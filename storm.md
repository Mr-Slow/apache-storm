### 1.简介
Apache Storm是由Twitter公司开源的一个分布式实时计算框架, 擅长进行实时数据流的处理, 并且可以和任何编程语言一起使用.
具有以下特点:
(1)易于与其他队列和数据库集成;
<br><br>
(2)易于使用: 只需定义3种抽象: spout, bolt, topology; 就可以实现处理和传递数据;
<br><br>
(3)易于扩展: 分布式运行, topo的每个部分都可以调整并发大小, 还有rebalance命令来动态调整并发量;
<br><br>
(4)较强的鲁棒性: 某个worker死掉会自动重启, 某个节点死掉该节点的worker会在另一个节点上重启;
<br><br>
(5)内部机制保证每条数据至少被处理一次;
<br><br>
(6)任何编程语言均可使用, 非java语言通过 "Multi-Language Protocol"与storm通信;
<br><br>
(7)易于部署和操作;

版本区别:

### 2.概念
(1)Nimbus: storm集群的master节点, 负责向各节点分发代码, 分配任务以及监控节点的运行状态;
<br><br>
(2)Supervisor: 每个工作节点运行一个supervisor进程, 负责接收nimbus指派的任务, 根据任务开启或停止worker进程, supervisor和nimbus通过zookeeper通信;
<br><br>
(3)Worker: 每个工作节点上具体执行数据处理逻辑的进程, 不同worker间通过Netty来通信;
<br><br>
(4)Topology: spout和bolt的连接图,规定数据的处理逻辑和传递路线, 不同机器上的多个worker组成topology;
<br><br>
(5)Executor: 每个worker下的1个线程称为executor, executor中执行一个或多个task;
<br><br>
(6)Task: 每个spout和bolt都会根据各自的并发量设置被当做一个或多个task执行;
<br><br>
(7)Spout: 产生数据源的具体逻辑, 可以自己生成或从外部读取;
<br><br>
(8)Bolt: 处理, 计算数据的具体逻辑;
<br><br>
(9)Tuple: storm的数据模型, 数据流中的基本处理单元;
<br><br>
(10)Groupings: tuple在各task间的分发策略: Shuffle grouping, Fields grouping等;

![storm1](/assets/storm1.png)

### 3.配置
常用有哪些
如何指定

### 4.Guaranteeing Message Processing容错机制
best effort, at least once, and exactly once through Trident.
msg_id

### 5.storm ui

### 6.运行问题

### 7. Storm Multi-Language Protocol

### 8. pacemaker

### 9. logviewer

### 10.运行模式

### 11.pystorm and streamparse, 调用原理

### 12. 序列化?
