from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)

    s = Select(browser.find_element(By.TAG_NAME, 'select'))
    s.select_by_visible_text(str(num1 + num2))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    sleep(30)
    browser.quit()