from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from formula import calc

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_id("input_value").text
y = calc(x)
input = browser.find_element_by_id("answer")
input.send_keys(y)
button = browser.find_element_by_id("solve")
button.click()
