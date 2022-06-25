"""
使用说明

将rabbitmq作为broker，rabbitmq信息如下：
用户名 compute_engine
密码 compute_engine
vhost compute_engine

1）在一个终端执行消费者 celery_consume_benchmark

celery -A celery_consume_benchmark worker --concurrency=50 -P gevent -l INFO -Q celery_benchmark

2）在另一个终端执行生产者 celery_publish_benchmark

执行python celery_consume_benchmark文件即可




"""

import time
import celery
from celery import platforms

platforms.C_FORCE_ROOT = True
# celery_app = celery.Celery('test_frame.test_celery.test_celery_app')
celery_app = celery.Celery()


class Config:
    # broker_url = f'redis://:123456@127.0.0.1:6379/7'  # 使用redis
    broker_url = f'amqp://compute_engine:compute_engine@localhost:5672/compute_engine'
    task_routes = {
        'task_fun': {"queue": "celery_benchmark", },
    }


celery_app.config_from_object(Config)


@celery_app.task(name='task_fun')
def task_fun(x):
    if x == 0:
        print(time.strftime("%H:%M:%S"), '消费第一条')
    if x == 99999:
        print(time.strftime("%H:%M:%S"), '消费第100000条')


if __name__ == '__main__':
    # 不需要使用命令行，直接启动此脚本。
    celery_app.worker_main(
        argv=['worker', '--pool=gevent', '--concurrency=50', '-n', 'worker1@%h', '--loglevel=DEBUG',
              '--queues=celery_benchmark'])
