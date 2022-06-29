import unittest
from utils import *
from read_data import *
from toolz import partition_all


class utilsTest(unittest.TestCase):

    # @unittest.skip
    def test_get_second_from(self):
        # 15: 42:33, 15: 46:21
        start = '2022-6-25 19:34:28'
        end = '2022-6-25 19:45:30'
        print('%ss' % get_second_from(start, end))

    @unittest.skip
    def test_model_IsolationForest(self):
        u_model = model_load(isolation_forest_model_path)
        data = fake_model_data()
        model, data, y_predict = modelML_use(u_model, data)
        print(y_predict)

    @unittest.skip
    def test_model_RandomForest(self):
        u_model = model_load(random_forest_model_path)
        data = fake_model_data()
        model, data, y_predict = modelML_use(u_model, data)
        print(y_predict)

    @unittest.skip
    def test_read_fake_model_data(self):
        cols, df_list = read_telemetry_params_for_model()
        p = partition_all(2, df_list)
        print(cols)
        for pp in list(p):
            print(list(pp))

    @unittest.skip
    def test_ModelFactory(self):
        print(id(ModelFactory()))
        print(id(ModelFactory()))


if __name__ == "__main__":
    unittest.main()
