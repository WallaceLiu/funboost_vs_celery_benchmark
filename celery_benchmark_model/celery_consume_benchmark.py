import time
import celery
from celery import platforms
from utils import *

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
    worker_disable_rate_limits = True
    task_acks_late = True
    worker_prefetch_multiplier = 4
    worker_cancel_long_running_tasks_on_connection_loss = True
    broker_heartbeat = 0
    broker_pool_limit = None
    broker_connection_timeout = 20
    broker_connection_retry = True
    broker_connection_max_retries = 3
    result_expires = 3600


celery_app.config_from_object(Config)

mf = ModelFactory()


@celery_app.task(name='task_fun')
def task_fun(x, columns, model_type):
    df = pd.DataFrame(data=x, columns=columns)
    mf.predict(model_type, df)
