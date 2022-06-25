# 使用说明

将rabbitmq作为broker，rabbitmq信息如下：
用户名 compute_engine
密码 compute_engine
vhost compute_engine

1）在一个终端执行消费者 celery_consume_benchmark

```shell script
celery -A celery_consume_benchmark worker --concurrency=50 -P gevent -l INFO -Q celery_benchmark
```

2）在另一个终端执行生产者 celery_publish_benchmark

执行文件即可
```shell script
python celery_consume_benchmark
```


- 发送消息 

18:56:26 发布第一条
18:58:00 发布第100000条

- 消费消息

18:56:26 发布第一条
18:58:19 消费第100000条

113


