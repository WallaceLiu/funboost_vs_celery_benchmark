import gevent.monkey;

gevent.monkey.patch_all()
import time
from funboost import task_deco, BrokerEnum, ConcurrentModeEnum


def rule(v):
    r = [0.8, 0.2]
    return v >= r[0] or v <= r[1]


@task_deco('dssf_benchmark', broker_kind=BrokerEnum.RABBITMQ_AMQPSTORM, log_level=1,
           concurrent_mode=ConcurrentModeEnum.GEVENT, )
def task_fun(x):
    # print('aaaaa' + x)
    if x == 0:
        print(time.strftime("%H:%M:%S"), '消费第一条')
    if x == 99999:
        print(time.strftime("%H:%M:%S"), '消费第100000条')
    for k in x[1].keys():
        rule(x[1][k])


if __name__ == '__main__':
    # task_fun.consume()
    task_fun.multi_process_consume(10)
