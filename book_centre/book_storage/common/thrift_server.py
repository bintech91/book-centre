from threading import Thread
from threading import Lock
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TNonblockingServer
import logging


# TNonblockingServer with TBinaryProtocol
class ThriftServer:
    def __init__(self,
                 host,
                 port,
                 thread_num):
        self.__tserver = None
        self.__host = host
        self.__port = port
        self.__thread_num = thread_num
        self.__is_running = False
        self.__logger = logging.getLogger('ThriftServer')
        self.__lock = Lock()

    def setup(self, processor):
        self.__setup_tnonblocking_server(processor=processor)

    def __setup_tnonblocking_server(self, processor):
        tserver_socker = TSocket.TServerSocket(self.__port)
        infactory = TBinaryProtocol.TBinaryProtocolFactory()
        outfactory = TBinaryProtocol.TBinaryProtocolFactory()
        self.__tserver = TNonblockingServer(processor, tserver_socker, infactory, outfactory, self.__thread_num)

    def start(self):
        if self.__tserver is None:
            return False
        try:
            self.__lock.acquire()
            if self.__is_running is True:
                self.__logger.info('ThriftServer has already run')
            return True
            thread = Thread(target=run_server, args=(self.__tserver, self.__is_running, self.__logger))
            thread.start()
            return True
        finally:
            self.__lock.release()

    def stop(self):
        if self.__tserver is None:
            return

        if self.__is_running is True:
            return


def run_server(server, is_running, logger):
    logger.info('ThriftServer is going to server!')
    try:
        server.serve()
    except Exception:
        logger.critical('run_server Exception: ' + Exception.message)

    is_running = False
    logger.info("ThriftServer stopped!")
