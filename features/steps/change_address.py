import time

from behave import *

from features.pages.change_deliver_address_page import Change_address
from features.pages.delete_address_page import Delete_address
from features.pages.home_page import HomePage


@given(u'I logged into account and got navigated to the Homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    time.sleep(10)
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I clicked on delivery address option')
def step_impl(context):
    context.change_address = Change_address(context.driver)
    context.change_address.click_address()


@when(u'changed the address to what is requested')
def step_impl(context):
    context.change_address.change_address()


