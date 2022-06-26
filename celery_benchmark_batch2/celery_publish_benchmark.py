import time
from celery_benchmark_batch2.celery_consume_benchmark import task_fun, celery_app, Config

from readdata import read_data

columns, data = read_data('/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')

print('start......')

for d in data:
    if d[0] == 0:
        print(time.strftime("%H:%M:%S"), '发布第一条')
    if d[0] == 9999:
        print(time.strftime("%H:%M:%S"), '发布第10000条')
    task_fun.delay(d)
