import time
from celery_benchmark_batch_concurrent.celery_consume_benchmark import task_fun, celery_app, Config
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
# r = redis.from_url(Config.broker_url)
# r.delete(Config.task_routes['task_fun']['queue'])
from read_data import partition_data

file_path = '/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv'
thread_pool = 10
chunk_size = 1000


def send(data):
    for d in data:
        # print(d[0])
        # if d[0] == 0:
        # print(time.strftime("%H:%M:%S"), '发布第一条')
        # if d[0] == 9999:
        # print(time.strftime("%H:%M:%S"), '发布第10000条')
        task_fun.delay(d)


col, data = partition_data(chunk_size, file_path)

print('start......')
executor = ThreadPoolExecutor(max_workers=thread_pool)
f_list = []
print(time.strftime("%H:%M:%S"), '发布第一条')
for d in list(data):
    future = executor.submit(send, d)
    f_list.append(future)
wait(f_list)
print(time.strftime("%H:%M:%S"), '发布最后一条')
