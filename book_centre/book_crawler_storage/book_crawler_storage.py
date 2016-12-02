import sys
sys.path.append('thrift_gen')

from storage_thrift_server import StorageThriftServer

def main():
    storage_thrift_server = StorageThriftServer()
    if storage_thrift_server.setup_and_start() is False:
        print 'Could not start thrift_server'


if __name__ == '__main__':
    main()