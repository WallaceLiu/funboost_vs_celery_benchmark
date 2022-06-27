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
        print(time.strftime("%H:%M:%S"), '消费第10000条')


if __name__ == '__main__':
    # 不需要使用命令行，直接启动此脚本。
    celery_app.worker_main(
        argv=['worker', '--pool=gevent', '--concurrency=50', '-n', 'worker1@%h', '--loglevel=DEBUG',
              '--queues=celery_benchmark'])
