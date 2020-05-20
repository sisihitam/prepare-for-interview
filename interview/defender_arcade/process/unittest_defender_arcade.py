import unittest
from defender_arcade import overlap

class TestDefenderArcade(unittest.TestCase):
    def test_success(self):
        self.assertEqual(overlap(925,1030,1010,1100), True)
        self.assertEqual(overlap(900,1030,1030,1100), False)

if __name__ == '__main__':
    unittest.main()