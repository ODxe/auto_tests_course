from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(number):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chestImage = browser.find_element(By.ID, 'treasure')
    x = chestImage.get_attribute('valuex')
    y = calc(x)

    inputAnswer = browser.find_element(By.ID, 'answer')
    inputAnswer.send_keys(y)

    robotCheck = browser.find_element(By.ID, 'robotCheckbox')
    robotCheck.click()
    robotRadio = browser.find_element(By.ID, 'robotsRule')
    robotRadio.click()

    submitButton = browser.find_element(By.TAG_NAME, 'button')
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
