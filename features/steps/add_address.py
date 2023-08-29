import time
from datetime import datetime

from behave import *

from features.pages.add_address_page import Add_address
from features.pages.home_page import HomePage


@given(u'I logged into my account and got navigated to Homepage')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    time.sleep(10)
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I click on my account and go to address option')
def step_impl(context):
    context.add_address = Add_address(context.driver)
    context.add_address.click_account()
    context.add_address.click_address()


@when(u'click on add a new address')
def step_impl(context):
    context.add_address.click_add_address()


@then(u'entered all the details and added it')
def step_impl(context):
    context.add_address.enter_name("Lokesh")
    time_stamp = datetime.now().strftime("%H")
    invalid_number = int("8105" + time_stamp + "676")
    context.add_address.enter_num(invalid_number)
    context.add_address.enter_pin("560041")
    context.add_address.enter_address1("near minar masjid jaynagar 4th block")
    context.add_address.enter_address2("marehalli 4th block")
    context.add_address.click_Add_address()
    assert context.add_address.verify_text("Address saved")
