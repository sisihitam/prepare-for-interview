import unittest
from sockspair import sockMerchant

class TestSocks(unittest.TestCase):

    def test_sum_testcase1(self):
        self.assertEqual(sockMerchant(9,[10,20,20,10,10,30,50,10,20]),3)

    def test_sum_testcase0(self):
        self.assertEqual(sockMerchant(10,[1,1,3,1,2,1,3,3,3,3]),4)

if __name__ == '__main__':
    unittest.main()
