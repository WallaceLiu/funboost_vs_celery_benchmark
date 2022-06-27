# import gevent.monkey;gevent.monkey.patch_all()
import time
from fb_benchmark2.fb_consume_benchmark import task_fun

from readdata import expand_not

columns, data = expand_not('/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')

print('start......')

task_fun.clear()

for d in data:
    if d[0] == 0:
        print(time.strftime("%H:%M:%S"), '发布第一条')
    if d[0] == 9999:
        print(time.strftime("%H:%M:%S"), '发布第10000条')
    task_fun.push(d)
