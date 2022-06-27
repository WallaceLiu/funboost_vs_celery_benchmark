"""


5000*10000=50000000



"""

import pandas as pd
import numpy as np
from toolz import partition_all


def read_data(file_path):
    """

    :param file_path: /Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv
    :return:
    """
    df = pd.read_csv(file_path,
                     encoding="ISO-8859-1")

    df['Time'] = pd.to_datetime(df['Time'])
    columns = [col for col in df.columns if 'Unnamed' not in col]
    df.drop(columns=['Unnamed: 0', 'Time'], axis=1, inplace=True)
    return columns, df


def expand_not(file_path):
    cols, df = read_data(file_path)
    data = []
    # df = df.iloc[0:20]
    for index, row in df.iterrows():
        dic = dict(row)
        data.append((index, dic))
    return read_data(file_path)


def expand(file_path):
    cols, df = read_data(file_path)
    data = []
    # df = df.iloc[0:20]
    for index, row in df.iterrows():
        dic = dict(row)
        for k in dic.keys():
            data.append((k, dic[k]))
    return cols, data


def partition_data(chunk_size, file_path):
    columns, data = expand_not(file_path)
    return columns, partition_all(chunk_size, data)
#
# #
# c, data = partition_data(10, '/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')
# print(c)
# d_l = list(data)
# d_l_0 = d_l[0]
# print('a')
# for d in list(data):
#     print(d)
#
# columns, data = read_data('/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')
# for d in data:
#     print(d)
