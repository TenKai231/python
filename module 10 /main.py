import unittest

class TestStringMethods(unittest.TestCase):
    # ini adalah test cara 1 
    def test_string(self):
        self.assertEqual('www.Dicoding.com'.strip('c.mow'), 'dicoding')

    
    # test case 2
    def test_isalnum(self):
        self.assertTrue('D0ding'.isalnum())
        self.assertFalse('D0d!ng!'.isalnum())

    # test case 3
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('Coding'),2)
        with self.assertRaises(ValueError):
            s.index('Coding')

if __name__ == '__main__':
    unittest.main()