from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False

binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

driver.get('http://seleniumhq.org/')

print (driver.title)

driver.quit()
