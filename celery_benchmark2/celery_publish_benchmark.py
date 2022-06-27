import time
# import redis
from celery_benchmark.celery_consume_benchmark import task_fun, celery_app, Config

# r = redis.from_url(Config.broker_url)
# r.delete(Config.task_routes['task_fun']['queue'])

# for i in range(100000):
#     if i == 0:
#         print(time.strftime("%H:%M:%S"), '发布第一条')
#     if i == 99999:
#         print(time.strftime("%H:%M:%S"), '发布第100000条')
#     task_fun.delay(i)


from readdata import expand_not

columns, df = expand_not('/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')
# msg = []
# for index, row in df.iterrows():
#     dic = dict(row)
#     msg.append(dic)

for i in range(100000):
    if i == 0:
        print(time.strftime("%H:%M:%S"), '发布第一条')
    if i == 99999:
        print(time.strftime("%H:%M:%S"), '发布第100000条')
    task_fun.delay(i)
