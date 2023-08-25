import time

from behave import *

from features.pages.add_bank_accountpage import add_Bank_AccountPage
from features.pages.home_page import HomePage


@given(u'I logged in and got navigated to Home page')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I click on my account and go to payment options and click on manage bank accounts')
def step_impl(context):
    context.add_bank_account = add_Bank_AccountPage(context.driver)
    context.add_bank_account.click_on_account()
    context.add_bank_account.click_payment_options()
    context.add_bank_account.click_manage_account()
    context.add_bank_account.click_add_new_account()


@when(u'I enter all the valid details')
def step_impl(context):
    context.add_bank_account.click_ifsc_yes()
    context.add_bank_account.enter_ifsc("SBIN0017793")
    context.add_bank_account.click_ifsc_confirm()
    time.sleep(5)
    context.add_bank_account.enter_holder_name("LokeshaaM")
    context.add_bank_account.enter_accountNo("35225598255")
    context.add_bank_account.enter_confirm_accountNo("35225598255")
    time.sleep(5)
    context.add_bank_account.Account_type()
    time.sleep(5)
    context.add_bank_account.click_save_account()


@then(u'account added message should be displayed')
def step_impl(context):

    assert context.verify_account_added("Account added")
