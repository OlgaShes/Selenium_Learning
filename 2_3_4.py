from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    sleep(30)
    browser.quit()
