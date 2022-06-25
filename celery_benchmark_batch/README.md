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

2）在另一个终端执行生产者 celery_publish_benchmark

执行文件即可
```shell script
python celery_consume_benchmark
```
# 测试结果

- 发送消息 
171秒，发送一万条，每条5000个点，每秒34条

- 消费消息
171秒，一万条，每次判断5000个点，每秒判断1470588个点

