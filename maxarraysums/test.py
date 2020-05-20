import unittest
from maxarraysums import maxSubsetSum

class TestSocks(unittest.TestCase):

    def test_sum_testcase1(self):
        self.assertEqual(maxSubsetSum([3,7,4,6,5]),13)
    
    def test_sum_testcase0(self):
        self.assertEqual(maxSubsetSum([3,5,-7,8,10]),15)

if __name__ == '__main__':
    unittest.main()
