from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Василий")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Сергеев")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@mail.com")

    currentDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currentDir, 'task_file.txt')

    fileUploader = browser.find_element(By.ID, "file")
    fileUploader.send_keys(filePath)

    submitButton = browser.find_element(By.TAG_NAME, "button")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
