import unittest


class MyTestCase(unittest.TestCase):
    # function type setup and teardown- setup-testa-teardown-setup-testb-teardown
    # def setUp(self):   #before test
    #     print("I am setUp")
    #
    # def tearDown(self): #after test
    #     print("I am tearDown")

    #classmethod-- setup-testa-testb-teardown
    @classmethod
    def setUpClass(self):
        print('SetUpClass')

    def tearDownClass(self):
        print('TearDownClass')

    def test_a(self):
        self.assertEqual(True, False,"This is true /false")

    def test_b(self):
        print("Something")
        self.assertEqual(True, True,"Both are True")
    def test_c(self):
        print("Something else")
        self.assertEqual(False, True," false/True")
    def test_d(self):
        print("Something else")
        self.assertEqual(False, False,"Both are false")


if __name__ == '__main__':
    unittest.main()
