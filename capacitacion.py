import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class GoogleSearch(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiM0Kn56_32AhX4SjABHVJnAaQQPAgI')

    def test_google_search(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('python')

        search_field.submit()

        welcome_python = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a/h3')

        self.assertTrue(welcome_python.is_displayed)

    def tearDown(self): 
        self.driver.implicitly_wait(10)
        self.driver.close()

if __name__ == "__main__": 
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name= 'capacitacion'))











