import unittest 
from addtest import AddTestCase
from subtest import SubTestCase

def my_suite():
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AddTestCase))
    suite.addTest(unittest.makeSuite(SubTestCase))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
