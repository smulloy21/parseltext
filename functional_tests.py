import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_blog(self):
        # Monty the Python loads up the page
        self.browser.get('http://localhost:8000')
        self.assertIn('ParselText', self.browser.title)

        # He sees a header that says 'My Blogs'
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Blogs', header_text)

        # He sees a form to create a new blog
        inputbox = self.browser.find_element_by_id('new_blog')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'New Blog')

        # He creates a new blog for movie reviews
        inputbox.send_keys('Movie Reviews')
        inputbox.send_keys(Keys.ENTER)

        # When he hits enter, the new blog appears in his list of blogs
        list = self.browser.find_element_by_id('blogs')
        list_items = list.find_elements_by_tag_name('li')
        self.assertTrue(any(list_item.text == 'Movie Reviews' for list_item in list_items))

if __name__ == '__main__':
    unittest.main()
