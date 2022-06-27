from utils import *
import unittest


class utilsTest(unittest.TestCase):
    # @unittest.skip
    def test_get_second_from(self):
        print('%ss' % get_second_from('2022-6-25 13:41:11', '2022-6-25 13:42:06'))

    def test_model(self):
        u_model = model_load(
            '/Users/cap/project/funboost_vs_celery_benchmark/87dc85bb-f1d4-11ec-baf4-9c7bef2d2962.pickle')
        print(u_model)


if __name__ == "__main__":
    unittest.main()
