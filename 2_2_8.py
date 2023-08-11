from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('Iv@my.ru')
    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    sleep(30)
    browser.quit()    