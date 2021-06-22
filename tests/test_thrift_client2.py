import thriftpy2

# 解析thrift文件
test_python = thriftpy2.load('test_thrift.thrift', module_name='test_python_thrift')

from thriftpy2.rpc import make_client

# 创建client
client = make_client(test_python.Test, 'localhost', 9090)

people = test_python.People(name='Alice', age=25)

# execute
client.print_people_info(people)
print('print people info success.')

res = client.add(2, 3)
print('add result: %s + %s=%s' % (2, 3, res))
