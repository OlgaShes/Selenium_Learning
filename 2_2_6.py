from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    res = str(math.log(abs(12*math.sin(x))))

    browser.find_element(By.ID, 'answer').send_keys(str(res))
    browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
finally:
    sleep(30)
    browser.quit()
