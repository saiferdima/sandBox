from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    time.sleep(1)
    browser.quit()


answer = math.log(int(time.time()))


@pytest.mark.parametrize('link_id', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
# @pytest.mark.parametrize('link_id', ["236895"])
def test_guest_should_see_login_link(browser, link_id):
    link = f"https://stepik.org/lesson/{link_id}/step/1"
    browser.get(link)
    input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea"))
    )
    input.send_keys(str(math.log(int(time.time()))))
    send_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button"))
    )
    send_button.click()
    result = WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.XPATH,"//pre"))
    )
    assert result.text == "Correct!","OPTIONAL MESSAGE  !!!!!!!!!!    : "+ result.text

