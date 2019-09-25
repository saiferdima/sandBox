from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    required_fields = ["First name","Last name" , "Email"]
    browser = webdriver.Chrome()
    browser.get(link)

    for field in required_fields:
       browser.find_element_by_xpath("//div[label[contains(text(),'"+field+"')]]/input").send_keys("testData")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()