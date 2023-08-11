from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    ch_box = browser.find_element(By.ID, "robotCheckbox")
    ch_box.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()



finally:
    time.sleep(30)
    browser.quit()   

