import unittest
from cc.add import add

class AddTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(add(1,2),444, "dumb bitch")

    def test_two(self):
        self.assertEqual(add(1,1),2)



if __name__ == '__main__':
    unittest.main()
