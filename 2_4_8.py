from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# 29.035577670310595

link = 'http://suninjuly.github.io/explicit_wait2.html'
br = webdriver.Chrome()

try:
    br.get(link)
    button = br.find_element(By.ID, 'book')
    WebDriverWait(br, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()
    x = br.find_element(By.ID, 'input_value').text
    br.find_element(By.ID, 'answer').send_keys(calc(x))
    br.find_element(By.ID, 'solve').click()

    alert = br.switch_to.alert
    answ = alert.text[-18:]
    print(answ)    
    alert.accept()

    
finally:
    sleep(30)
    br.quit()