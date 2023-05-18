from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'/usr/bin/firefox')
browser.get('http://localhost:8000/')

assert 'Django' in browser.title