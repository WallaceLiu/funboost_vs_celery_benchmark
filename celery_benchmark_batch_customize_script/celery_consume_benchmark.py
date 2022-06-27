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
    task_ignore_result = True
    worker_prefetch_multiplier = 1000
    worker_disable_rate_limits = True
    task_acks_late = True


celery_app.config_from_object(Config)


def rule(v):
    r = [0.8, 0.2]
    return v >= r[0] or v <= r[1]


@celery_app.task(name='task_fun')
def task_fun(x):
    """

    每次判读5000个点

    :param x:
    :return:
    """
    # i = x[0]
    # if i == 0:
    #     print(time.strftime("%H:%M:%S"), '消费第一条')
    # if i == 9999:
    #     print(time.strftime("%H:%M:%S"), '消费第10000条')
    # for k in x[1].keys():
    rule(x[1])


if __name__ == '__main__':
    # 不需要使用命令行，直接启动此脚本。
    celery_app.worker_main(
        argv=['worker', '--pool=gevent', '--concurrency=50', '-n', 'worker1@%h', '--loglevel=DEBUG',
              '--queues=celery_benchmark'])
