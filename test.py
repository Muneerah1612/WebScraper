import unittest
from analyse import CheckUrl


class TestWebAnalysis(unittest.TestCase):
    def test_correct_url(self):
        test_param = 'https://www.python.org/'
        result = CheckUrl.ValidUrl()
        self.assertEqual(result, test_param)

    
if __name__ == '__main__':
    unittest.main()