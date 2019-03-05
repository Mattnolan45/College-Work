import unittest
from cc.sub import sub

class SubTestCase(unittest.TestCase):

    def test_one(self):
        self.assertNotEqual(sub(1,2),1)


if __name__=='__main__':
    unittest.main()
