import thriftpy2

# 解析thrift文件
test_python = thriftpy2.load('test_thrift.thrift', module_name='test_python_thrift')

from thriftpy2.rpc import make_server


class FunctionHandler:

    # 定义同名函数
    def print_people_info(self, people):
        print(people.name, people.age)

    def add(self, number1, number2):
        return number1 + number2

server = make_server(test_python.Test, FunctionHandler(), 'localhost', 9090)
print('server started...')
server.serve()