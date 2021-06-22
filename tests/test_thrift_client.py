from test_python import Test
from test_python.ttypes import People

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol
    client = Test.Client(protocol)

    # Make peple instane
    people = People(name='Alice', age=15)

    # Connect
    transport.open()

    # execute
    client.print_people_info(people)
    print('print people info success.')

    res = client.add(2, 3)
    print('add result: %s + %s=%s' % (2, 3, res))

    # Close
    transport.close()


main()