from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/simple_form_find_task.html"
link = "http://suninjuly.github.io/selects1.html"
import math




try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    num3 =str(num1+num2)
    print(num3)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(num3)


    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла