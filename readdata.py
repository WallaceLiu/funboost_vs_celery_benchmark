import pandas as pd
import numpy as np
from toolz import partition_all

def read_data(file_path):
    """

    :param file_path: /Users/cap/Documents/3.项目/二室/样例数据/遥测数据1-fake.csv'
    :return:
    """
    df = pd.read_csv(file_path,
                     encoding="ISO-8859-1")

    df['Time'] = pd.to_datetime(df['Time'])
    # df = df.iloc[0:10]
    columns = [col for col in df.columns if 'Unnamed' not in col]

    # for index, row in df.iterrows():
    #     dic = dict(row)
    #     print(dic.keys())
    return columns, df


def send_data(file_path):
    return read_data(file_path)


def partition_data(chunk,l):
    return  partition_all(chunk, dpu_df.values.tolist()))
