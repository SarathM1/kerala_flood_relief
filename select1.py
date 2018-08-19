import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


class Drpdowm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_drpdown(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://savealife.in/')

        s1 = Select(driver.find_element_by_id('district'))
        # print(s1.options)
        for opt in s1.options:
            s1.select_by_visible_text('Ernakulam')
        sleep(5)

        s2 = Select(driver.find_element_by_id('camp'))
        for option in s2.options:
            print(option.text, option.get_attribute('value'))

        for opt in s2.options:
            # s2.select_by_value('23')
            # s2.select_by_index(1)
            s2.select_by_visible_text('Little Flower Institute')

    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
