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
    data = []

    # df = df.iloc[0:10]
    for index, row in df.iterrows():
        dic = dict(row)
        data.append((index, dic))
    return columns, data


def send_data(file_path):
    return read_data(file_path)


#
# def partition_data(chunk, l):
#     return partition_all(chunk, l.values.tolist())

#
# columns, data = read_data('/Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv')
# for d in data:
#     print(d)
#
# start = pd.to_datetime('2022-6-25 18:56:00')
# end = pd.to_datetime('2022-6-25 18:56:26')
# print(end - start)
