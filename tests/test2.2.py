from selenium import webdriver
from formula import calc
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
firstname = browser.find_element_by_name("firstname")
lastname = browser.find_element_by_name("lastname")
email = browser.find_element_by_name("email")
file = browser.find_element_by_id("file")
firstname.send_keys("firstname")
lastname.send_keys("lastname")
email.send_keys("email@t.com")

file.send_keys(file_path)



button = browser.find_element_by_tag_name("button")
button.click()

assert True