from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    pic = browser.find_element(By.TAG_NAME, 'img')
    x = pic.get_attribute('valuex')
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    sleep(30)
    browser.quit()