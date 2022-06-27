# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:33:17 2021
对应tempo2中模型管理的其他部分 
跟模型分类 聚类 异常检测等无关
1、模型读取
2、模型输出
3、模型利用（分为机器学习ML和深度学习DL）
@author: HP
"""
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

'''1、模型读取'''


def model_load(path):
    '''
    选择路径和文件类型，将模型导入
    Args:
        path:模型的路径
        typer：模型存储的文件格式
    return:model
    0528
    '''
    typer = path.split('.')[1]
    if typer == 'pickle':
        model_path = path
        f = open(model_path, "rb")
        model = pickle.load(f)
        return (model)
    elif typer == 'h5':
        model_path = path
        model = load_model(model_path)
        return model
    '''
    elif typer=='pkl':
        model_path=path
        model=joblib(model_path)
        return model
    '''


'''2、模型输出'''


def model_dump(adet_Model, path, typer='pickle'):
    '''
    选择路径和文件类型，将模型导出
    Args:
        adet_Model：模型对象 object
        path:模型的存储路径
        typer：模型存储的文件格式
        0528
        open 必须打开一个文件而不是文件目录
    '''
    if typer == 'pickle':
        model_path = path + '\model.' + typer
        f = open(model_path, "wb")
        pickle.dump(adet_Model, f)
    elif typer == 'h5':
        model_path = path + '\model.' + typer
        adet_Model.save(model_path)


'''3、ML模型利用'''


def modelML_use(model, data, values_col=None):
    '''选择路径和文件类型，将模型导入
    Args:
        adet_Model：模型对象 object
        data:df结构数据 必须保证特征样本的维度和模型训练时的维度一致，否则识别不了
        values_col=None,数据
    Return:
        model,data,y_pred(原始数据和模型主要是为了后续评估)
        对于ML分类模型 y_pred是
        0528
    '''
    if isinstance(data, pd.DataFrame):
        if values_col == None:
            test_data = data.values
        else:
            test_data = data[values_col].values
            y_predict = model.predict(test_data)
        y_pred = pd.DataFrame(y_predict, columns=['y_pred'])
        return (model, data, y_pred)
    else:
        pass


'''4、DL模型利用'''


def modelDL_use(model, data, model_typer="lstm", typer="sequential_predict", var_col=None):
    """
    使用训练好的深度学习模型对特征数据集进行预测（不特指时间序列预测)
    :param model: object,待使用的深度学习模型
    :param data: df，待使用该模型的特征样本数据（默认无标签）
    :param model_typer:str,选择加载的深度模型的具体的算法类型。可选：'lstm'和'cnn'。
    :param typer:可选'sequential_predict'和’Feature_label_set'。'sequential_predict'表示选择时序预测，’Feature_label_set'表示选择多维特征与标签的预测。
    :param var_col:list,元素为str,特征数据列对应的列名组成的列表，默认空表示除了最后一列/行之外的均为特征数据列

    :return:
           model:待使用的机器学习模型(object)
           data:待使用该模型的特征样本数据（默认无标签）(DataFrame)
           y_pred:结果集(DataFrame)
    by huazhe
    """

    if isinstance(data, pd.DataFrame):  # 判断数据是否为df格式
        if var_col == None:  #
            test_data = data.values
        else:
            test_data = data[var_col].values
        if typer == "sequential_predict":  # 判断数据是否为时序数据
            Feature_dim = 1  # 特征维数为1
            test_data = test_data.reshape(1, -1)  # 将时序数据转换为1行多列的形式，代表一个样本输入
            Inputstep = test_data.shape[1]
        elif typer == "Feature_label_set":
            Feature_dim = test_data.shape[1]
            Inputstep = test_data.shape[0]
        if model_typer == "lstm":
            x_test = np.reshape(test_data, (test_data.shape[0], Feature_dim, Inputstep))
        elif model_typer == "cnn":
            x_test = np.reshape(test_data, (test_data.shape[0], Inputstep, Feature_dim))
        y_predict = model.predict(x_test)  # 将模型对测试数据进行预测
        y_predict = y_predict.reshape(-1, 1)
        # y_predict=pd.DataFrame(y_predict,columns=["y_predict"])
        y_predict = pd.DataFrame(y_predict, columns=["y_pred"])
        return (model, data, y_predict)
    else:
        pass


u_model = model_load('87dc85bb-f1d4-11ec-baf4-9c7bef2d2962.pickle')

print(u_model)
