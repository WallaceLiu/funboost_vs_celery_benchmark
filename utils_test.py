from utils import *
import unittest


class utilsTest(unittest.TestCase):
    @unittest.skip
    def test_get_second_from(self):
        print('%ss' % get_second_from('2022-6-25 13:41:11', '2022-6-25 13:42:06'))

    @unittest.skip
    def test_model_load(self):
        u_model = model_load(
            '/Users/cap/project/funboost_vs_celery_benchmark/d1a2cc7a-c3bf-11ec-b8a6-67f88aaa7c62.pickle')
        print(u_model)

    @unittest.skip
    def test_model_IsolationForest(self):
        u_model = model_load(
            '/Users/cap/project/funboost_vs_celery_benchmark/d1a2cc7a-c3bf-11ec-b8a6-67f88aaa7c62.pickle')
        data = create_data()
        model, data, y_predict = modelML_use(u_model, data)
        print(y_predict)

    def test_model_RandomForest(self):
        u_model = model_load(
            '/Users/cap/project/funboost_vs_celery_benchmark/87dc85bb-f1d4-11ec-baf4-9c7bef2d2962.pickle')
        data = create_data()
        model, data, y_predict = modelML_use(u_model, data)
        print(y_predict)


if __name__ == "__main__":
    unittest.main()
