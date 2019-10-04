from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
link = "http://suninjuly.github.io/cats.html"

browser.get(link)

browser.find_element_by_id("button")