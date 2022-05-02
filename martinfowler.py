import time
from OpenSSL.rand import status
from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path='/Users/rmlamont/Web Driver/chromedriver')


@when('open Aquabot homepage')
def openHomePage(context):
    context.driver.get("https://martinfowler.com/")
    time.sleep(10)


@then('verify logo is displayed on homepage')
def verifyLogo(context):
    context.driver.find_element_by_xpath(" //header/div[1]/a[1]/img[1]").is_displayed()
    assert status is True


@then('close chrome browser')
def closeBrowser(context):
    context.driver.Close()
