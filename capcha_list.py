from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstNumber = int(browser.find_element(By.ID, "num1").text)
    secondNumber = int(browser.find_element(By.ID, "num2").text)
    answer = firstNumber + secondNumber

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))

    submitButton = browser.find_element(By.TAG_NAME, 'button')
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
