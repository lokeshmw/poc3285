import time

from behave import *

from features.pages.delete_address_page import Delete_address
from features.pages.home_page import HomePage


@given(u'I logged in into my account and got navigated to Homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    time.sleep(10)
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I clicked on my account and then to address option')
def step_impl(context):
    context.delete_address = Delete_address(context.driver)
    context.delete_address.click_account()
    context.delete_address.click_address()


@when(u'deleted a address which is requested')
def step_impl(context):
    context.delete_address.delete_address()


@then(u'validating the deleted message')
def step_impl(context):
    assert context.delete_address.verify_text()
