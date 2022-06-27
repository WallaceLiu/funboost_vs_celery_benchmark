import pandas as pd
import numpy as np
from toolz import partition_all


def get_second_from(start, end):
    """

    :param start:  2022-6-25 13:41:11
    :param end:  2022-6-25 13:42:06
    :return:
    """
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    r = end - start
    return r.seconds

