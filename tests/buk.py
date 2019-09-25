from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
link = "http://qa61.friendly-tech.com/CPEAdminQA6_1/Login.aspx"
text = "Friendly One-IoT"
topMenuNames = ["CPE Profile", "Update a CPE", "Update Group", "Monitoring", "Event Monitoring", "Reports",
                "File Management", "Settings"]

try:
    browser.implicitly_wait(5)
    browser.get(link)
    name = browser.find_element_by_id("txtName")
    password = browser.find_element_by_id("txtPassword")
    submit = browser.find_element_by_id("btnLogin_btn")

    name.send_keys("")
    password.send_keys("")
    submit.click()
    pageName = browser.find_element_by_id("lblTitle1").text
    assert pageName == text
    browser.find_element_by_xpath("//td[@topmenu = '" + topMenuNames[2] + "']").click()
    browser.switch_to.frame("frmDesktop")
    table = browser.find_element_by_id("tblParameters")
    total = int(browser.find_element_by_id("pager2_lblCount").text)
    assert table.is_displayed()
    assert total>0
finally:
    time.sleep(5)
    browser.quit()

assert True
