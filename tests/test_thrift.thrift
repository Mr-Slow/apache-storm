# 定义name space
namespace py test_python
namespace java test_java

# 定义数据类型
struct People {
    1: string name,
    2: i32 age
}

# 定义service
service Test {
    void print_people_info(1:People people),

    i32 add(1:i32 number1, 2:i32 number2)
}
