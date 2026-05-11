from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    newWindow = browser.window_handles[1]
    browser.switch_to.window(newWindow)

    x = float(browser.find_element(By.ID, "input_value").text)
    answer = math.log(abs(12 * math.sin(x)))

    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(str(answer))

    submitButton = browser.find_element(By.TAG_NAME, "button")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
