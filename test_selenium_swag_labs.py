# Given user opens the website
#  And cookies are accepted  //no cookies
# When user clicks input username
#  And user inserts username
#  And user clicks input password
#  And user inserts password
#  And user clicks enter
# Then user is logged in = cart button is available
# Given the user is logged in
# When user clicks "Add to cart" button
# Then number at cart icon shows "1"
#  And Cart shows proper product and proper qty

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def test_can_add_to_cart():
    """User logs in and adds 1 product to cart"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    url = 'https://www.saucedemo.com/'
    user = 'standard_user'
    password = 'secret_sauce'

    driver.get(url)
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.click()
    username_input.send_keys(user)

    password_input = driver.find_element(By.ID, 'password')
    password_input.click()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    try:
        cart_button = driver.find_element(By.ID, 'shopping_cart_container')
    except NoSuchElementException:
        assert False
    else:
        assert True

    add_to_cart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart.click()
    cart_qty = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_qty.text == '1'
    cart_button.click()

    try:
        added_product = driver.find_element(By.ID, 'item_4_title_link')
    except NoSuchElementException:
        assert False
    else:
        assert True

    assert added_product.text == 'Sauce Labs Backpack'
    product_qty = driver.find_element(By.CLASS_NAME, 'cart_quantity')
    assert product_qty.text == '1'
