import unittest
from countingvalleys import countingValleys

class TestCountingValleys(unittest.TestCase):
    def test_sum_testcase0(self):
        self.assertEqual(countingValleys(8,'UDDDUDUU'),1)
    
    def test_sum_testcase1(self):
        self.assertEqual(countingValleys(12,'DDUUDDUDUUUD'),2)

if __name__ == '__main__':
    unittest.main()
