from behave import *

from features.pages.home_page import HomePage
from features.pages.transaction_page import transaction_Page


@given(u'I logged in to my account and got navigated to Home page')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()
    context.login_page.enter_phone("8105000676")
    context.login_page.enter_password("Loki@1234")
    context.verify_login = context.login_page.click_on_login()


@when(u'I click on my account and go to amazon pay option')
def step_impl(context):
    context.transactions_history = transaction_Page(context.driver)
    context.transactions_history.click_account()
    context.transactions_history.click_amazon_pay()


@when(u'click on transactions')
def step_impl(context):
    context.transactions_history.click_amazon_symbol()
    context.transactions_history.click_transaction_xpath()


@then(u'all transactions are printed')
def step_impl(context):
    a = context.transactions_history.print_transactions()
    print(a)
    assert len(a) != 0

