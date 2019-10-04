from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from formula import calc
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"




try:
    browser.get(link)
    button2 = browser.find_element_by_xpath("//button")
    button2.click()
    second_window_name = browser.window_handles[1]
    browser.switch_to.window(second_window_name)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла