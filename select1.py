import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from bs4 import BeautifulSoup
import pprint
import re
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import pandas as pd
pp = pprint.PrettyPrinter()

DISTRICT = 'Ernakulam'


def wait_for_condition(driver, value=0):
    element = driver.find_element_by_id('count').text
    element = int(element.partition(' ')[0])
    if(element != value):
        return
    sleep(1)


def parse_data(text):
    temp_list = []
    soup = BeautifulSoup(''.join(text), features='html.parser')
    for i in soup.prettify().split('<hr/>'):
        soup_temp = BeautifulSoup(''.join(i), features='html.parser')
        x = soup_temp.find_all('p')
        temp_l2 = []
        temp_dict = {}
        for each_elem in x:
            lines = each_elem.getText().strip().splitlines()
            temp_l2.append(lines[2].strip())
        if len(x) > 0:
            temp_dict['updated'] = temp_l2[0]
            temp_dict['item'] = temp_l2[1]
            temp_list.append(temp_dict)
            # print '~' * 30
    return pd.DataFrame(temp_list)


def read_inner(driver):
    outer_div = driver.find_element_by_id("cart")
    inner_html = outer_div.get_attribute('innerHTML')
    return inner_html


def write_to_file(df, district, camp_name):
    ''' Remove illegal characters from fileName '''
    temp_str = district + '_' + camp_name
    fName = re.sub(r'[\\/*?:"<>|]', "", temp_str)
    fName = fName + '.csv'
    df.to_csv(fName)


class Drpdowm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_drpdown(self):
        self.driver.maximize_window()
        self.driver.get('http://savealife.in/')

        # Read initial value of span 'count'
        init_val = self.driver.find_element_by_id('count').text
        init_val = int(init_val.partition(' ')[0])

        # Update value of 'district'
        s1 = Select(self.driver.find_element_by_id('district'))
        s1.select_by_visible_text(DISTRICT)

        sleep(1)
        # Wait for value of span 'count' to update
        # wait_for_condition(self.driver, init_val)

        # Select values of camp
        s2 = Select(self.driver.find_element_by_id('camp'))
        for option in s2.options:
            camp_name = option.text
            print(camp_name)
            # Skip default value of 'camp'
            if camp_name == 'Select Camp':
                continue
            s2.select_by_visible_text(camp_name)
            print 'Sleeping for 3 seconds'
            sleep(1)
            inner_html = read_inner(self.driver)
            df = parse_data(inner_html)

            try:
                df['updated'] = pd.to_datetime(df.updated)
                df = df.sort_values(by='updated', ascending=False)
            except AttributeError as e:
                print 'No data available!!'
                print e

            write_to_file(df, DISTRICT, camp_name)

    def tearDown(self):
        sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
