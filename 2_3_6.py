from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
br = webdriver.Chrome()

try:
    # Открываем окно с ссылкой
    br.get(link)
    # Клик по кнопке
    br.find_element(By.TAG_NAME, 'button').click()
    # Переходим на новую вкладку 
    br.switch_to.window(br.window_handles[1])
    # Находим на странице х
    x = br.find_element(By.ID, 'input_value').text
    # Вводим ответ в поле
    br.find_element(By.ID, 'answer').send_keys(calc(x))
    # Нажимаем кнопку
    br.find_element(By.TAG_NAME, 'button').click()

finally:
    sleep(30)
    br.quit()
