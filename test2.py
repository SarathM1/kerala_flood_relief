from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox.sh')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('http://seleniumhq.org/')

print (driver.title)

driver.quit()
