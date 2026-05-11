from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill():
    # функция для заполнения формы
    inputFirstName = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    inputFirstName.send_keys("Сергей")
    inputSecondName = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    inputSecondName.send_keys("Петров")
    inputEmail = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    inputEmail.send_keys("test@mail.ru")
    inputPhone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    inputPhone.send_keys("+79009999999")
    inputAddress = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    inputAddress.send_keys("Russia")

try:
    link1 = "https://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    # Тест по первой ссылке (работающий корректно)
    fill() #заполнить форму

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    # Тест по второй ссылке (с ошибкой)

    browser.get(link2)

    fill()  # заполнить форму

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
