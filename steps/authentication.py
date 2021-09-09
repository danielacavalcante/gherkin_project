from behave import *
from nose.tools import *
from selenium.webdriver.common.by import By
from factory.locators import MainPageLocator
from factory.locators import SearchPageLocator
from factory.locators import BrowsePageLocator

@given(u'I access database questions site')
def step_impl(context):
    context.browser.get("https://opentdb.com/")
    assert_true(context.browser.find_element(*MainPageLocator.BROWSE_BTN))

@when(u'I search a question "Science:"')
def step_impl(context):
    context.browser.find_element(*MainPageLocator.BROWSE_BTN).click()
    context.browser.find_element(*SearchPageLocator.SEARCH_FIELD).send_keys("Science:")
    context.browser.find_element(*SearchPageLocator.SEARCH_BTN).click()

@when(u'I search a valid question "Is Tartu the capital of Estonia?"')
def step_impl(context):
    context.browser.find_element(*MainPageLocator.BROWSE_BTN).click()
    context.browser.find_element(*SearchPageLocator.SEARCH_FIELD).send_keys("Is Tartu the capital of Estonia?")
    context.browser.find_element(*SearchPageLocator.SEARCH_BTN).click()

@when(u'I search in category for "Science: Computers"')
def step_impl(context):
    context.browser.find_element(*MainPageLocator.BROWSE_BTN).click()
    context.browser.find_element(*SearchPageLocator.SEARCH_FIELD).send_keys("Science:")
    context.browser.find_element(*SearchPageLocator.CHOOSE_BTN).click()
    context.browser.find_element(*SearchPageLocator.CHOOSE_BTN).send_keys("C")
    context.browser.find_element(*SearchPageLocator.SEARCH_BTN).click()


@then(u'I must see a message error')
def step_impl(context):
    assert_equal("No questions found.", context.browser.find_element(*BrowsePageLocator.ERROR_MSG).text)

@then(u'I see the "Is Tartu the capital of Estonia?" question')
def step_impl(context):
    assert_equal("Is Tartu the capital of Estonia?", context.browser.find_element(*BrowsePageLocator.VALID_QUESTION).text)

@then(u'I see 25 result list')
def step_impl(context):
    assert_equal("Science: Computers", context.browser.find_element(*BrowsePageLocator.FIRST_ITEM_SEARCH).text)
    assert_equal("Science: Computers", context.browser.find_element(*BrowsePageLocator.TWENTY_FIFTH_ITEM_SEARCH).text)

@then(u'I see page control')
def step_impl(context):
    assert_true(context.browser.find_element(*BrowsePageLocator.PAGE_CONTROL))





