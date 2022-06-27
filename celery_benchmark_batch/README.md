# 使用说明
将rabbitmq作为broker，rabbitmq信息如下：
```text
用户名 compute_engine
密码 compute_engine
vhost compute_engine
```
1）在一个终端执行消费者 celery_consume_benchmark

```shell script
celery -A celery_consume_benchmark worker --concurrency=50 -P gevent -l INFO -Q celery_benchmark
```
或
```shell script
nohup celery -A celery_consume_benchmark worker --concurrency=50 -P gevent -l INFO -Q celery_benchmark > celery_benchmark_log.log 2>&1 &
```

2）在另一个终端执行生产者 celery_publish_benchmark，命令如下
```shell script
python celery_consume_benchmark.py
```
# 测试结果
- MacBook Pro (15-inch, 2019)
- 2.3 GHz 八核Intel Core i9
- 16 GB 2400 MHz DDR4
- 并发为50
- 10000条消息，每条5000个数据点，共计50000000
- 每次判断5000个点数据点
- 单队列

-|线程|耗时(s)|每秒|备注
---|---|---|---|---
生产消息|50|184|54条|gevent,concurrency=50,ack
消费消息|50|-|282485点|gevent,concurrency=50,ack
生产消息|100|131|76条|gevent,concurrency=100,ack
消费消息|100|-|381679点|gevent,concurrency=100,ack
生产消息|500|119|84条|gevent,concurrency=500,ack
消费消息|500|-|420168点|gevent,concurrency=500,ack
生产消息|1000|116|86条|gevent,concurrency=500,ack
消费消息|1000|-|431034点|gevent,concurrency=500,ack




[系统资源](../pictures/WX20220626-123839@2x.png)
