import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_blog(self):
        # Monty the Python loads up the page
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.main()
