from selenium import webdriver
from formula import calc
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_id("input_value").text
answer = browser.find_element_by_id("answer")
robotCheckbox = browser.find_element_by_id("robotCheckbox")

robotsRule = browser.find_element_by_id("robotsRule")
y = calc(x)
answer.send_keys(y)
robotCheckbox.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)




button.click()

assert True