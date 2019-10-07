import pytest
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.smoke
@pytest.mark.regression
def test_guest_should_see_login_link(browser):
    browser.get(link)
    add_to_basket_button= browser.find_element_by_xpath("//div[@class = 'row']//button[@type= 'submit']")
    assert add_to_basket_button.is_displayed(), "add_to_basket_button  Not Displayed"
