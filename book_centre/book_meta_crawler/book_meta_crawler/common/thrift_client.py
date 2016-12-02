from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import logging


class ThriftClient:
    def __init__(self,
                 host,
                 port,
                 client_factory,
                 num_retries):
        self.__host = host
        self.__port = port
        self.__factory = client_factory
        self.__num_retries = num_retries
        self.__logger = logging.getLogger('ThriftClient')

    def get_client(self):
        try:
            # make socket
            tsocket_transport = TSocket.TSocket(self.__host, self.__port)
            self.__transport = TSocket.TFramedTransport(tsocket_transport)
            self.__protocol = TBinaryProtocol.TBinaryProtocol(self.__transport)
            self.__client = self.__factory(self.__protocol)
            # Connect!
            self.__transport.open()
            return self.__client
        except Thrift.TException, tx:
            self.__logger.exception('ThriftClient: ' + tx.message)
            return None

    def get_num_retries(self):
        return self.__num_retries
    
    def close(self):
        if self.__transport is not None:
            self.__transport.close()
