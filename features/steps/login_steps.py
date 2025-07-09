from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import allure
import json

@given('the user is on the saucedemo login page')
def step_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('the user logs in')
def step_user_logs_in(context):
    username = context.test_data[0]["username"]
    password = context.test_data[0]["password"]
    context.login_page.login(username, password)

@when('the user logs in with username "{username}" and password "{password}"')
def step_user_logs_in_with_params(context, username, password):
    context.login_page.login(username, password)

@then('the user should see the products page')
def step_user_sees_products(context):
    title = context.login_page.get_title()
    if title != "Products":
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
    assert title == "Products"
    context.driver.quit()

@then('the user should see an error message')
def step_user_sees_error(context):
    try:
        error_element = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h3[contains(@data-test,'error')]")
            )
        )
        error_text = error_element.text
    except Exception:
        error_text = ""
    
    if "Epic sadface" not in error_text:
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)

    assert "Epic sadface" in error_text, "Error message not displayed!"
    context.driver.quit()
