import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


def wait_for_condition(driver, value=0):
    element = driver.find_element_by_id('count').text
    element = int(element.partition(' ')[0])
    if(element != value):
        return
    sleep(1)


class Drpdowm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_drpdown(self):
        self.driver.maximize_window()
        self.driver.get('http://savealife.in/')

        init_val = self.driver.find_element_by_id('count').text
        init_val = int(init_val.partition(' ')[0])
        s1 = Select(self.driver.find_element_by_id('district'))
        for opt in s1.options:
            s1.select_by_visible_text('Ernakulam')

        wait_for_condition(self.driver, init_val)

        s2 = Select(self.driver.find_element_by_id('camp'))
        for option in s2.options:
            print(option.text, option.get_attribute('value'))
            text = option.text
            if text == 'Select Camp':
                continue
            s2.select_by_visible_text(text)
            break

    def tearDown(self):
        sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
