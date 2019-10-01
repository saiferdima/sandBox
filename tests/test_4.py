from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    answer_input = browser.find_element_by_id("answer")
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robots_rule = browser.find_element_by_id("robotsRule")
    button = browser.find_element_by_css_selector("button.btn")
    y = calc(x)
    answer_input.clear()
    answer_input.send_keys(y)
    robot_checkbox.click()
    robots_rule.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла