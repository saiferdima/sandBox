import unittest


class TestAbs(unittest.TestCase):
    # def test_abs1(self):
    #     self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
    #
    # def test_abs2(self):
    #     self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
    def test_some1(self):
        from selenium import webdriver
        import time

        try:
            link = "http://suninjuly.github.io/registration1.html"
            required_fields = ["First name", "Last name", "Email"]
            browser = webdriver.Chrome()
            browser.get(link)

            for field in required_fields:
                browser.find_element_by_xpath("//div[label[contains(text(),'" + field + "')]]/input").send_keys(
                    "testData")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()




    def test_some2(self):
        from selenium import webdriver
        import time

        try:
            link = "http://suninjuly.github.io/registration2.html"
            required_fields = ["First name", "Last name", "Email"]
            browser = webdriver.Chrome()
            browser.get(link)

            for field in required_fields:
                browser.find_element_by_xpath("//div[label[contains(text(),'" + field + "')]]/input").send_keys(
                    "testData")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()



if __name__ == "__main__":
    unittest.main()