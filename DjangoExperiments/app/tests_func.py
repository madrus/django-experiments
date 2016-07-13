from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # Selenium may wait up to 3 sec if something is not found


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("Home Page - My Django Application", self.browser.title) 
       #self.fail("Finish the test!") 


if __name__ == '__main__':
    unittest.main()
