from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Firefox(options=options)
driver.get('http://127.0.0.1:8000')