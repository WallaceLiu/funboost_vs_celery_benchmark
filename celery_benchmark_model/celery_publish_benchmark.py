import time
from celery_benchmark_model.celery_consume_benchmark import task_fun, celery_app, Config
from toolz import partition_all
from read_data import read_telemetry_params_for_model
from utils import models

print(models.keys())

columns, data = read_telemetry_params_for_model()

data_partition = partition_all(5000, data)

print('start......')

print(time.strftime("%H:%M:%S"), '发布第一条')
for p in list(data_partition):
    task_fun.delay(p, columns, 'isolation_forest')
print(time.strftime("%H:%M:%S"), '最后第一条')
