from test_python import Test

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class FunctionHandler:

    # 定义同名函数
    def print_people_info(self, people):
        print(people.name, people.age)

    def add(self, number1, number2):
        return number1 + number2


if __name__ == '__main__':
    # handler封装入Test中
    hander = FunctionHandler()
    processor = Test.Processor(hander)

    # 创建socket和server
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # 启动server
    print('server started...')
    server.serve()


