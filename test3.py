#!/home/teroot/python3_virtual_env/flood_app/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging


def get_profile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile

def main():
    browser = webdriver.Firefox(firefox_profile=get_profile())

    #browser shall call the URL
    browser.get("http://www.google.com")
    time.sleep(5)
    browser.quit()

if __name__ == "__main__":
    main()
