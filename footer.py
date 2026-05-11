from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = " https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    answer = math.log(abs(12) * math.sin(int(x)))

    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(str(answer))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robotCheck = browser.find_element(By.ID, "robotCheckbox")
    robotCheck.click()

    robotRadio = browser.find_element(By.ID, "robotsRule")
    robotRadio.click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
