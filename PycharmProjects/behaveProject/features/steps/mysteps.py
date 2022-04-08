import time
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('open a browser')
def openBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(5)
    context.driver.maximize_window()



@when('user is on login page')
def loginPage(context):
    context.driver.get(r"https://www.booking.com/index.html?aid=2167732&label=37813b10aa9511ec943f05db9830e5b8")
    time.sleep(2)

@when('user enters "{Username}" and "{Password}"')
def enterUsername(context,Username,Password):
     context.driver.find_element_by_xpath("//a[@class='bui-button bui-button--secondary js-header-login-link']").click()
     username = context.driver.find_element_by_id("username")
     username.click()
     username.send_keys(Username)
     submit = context.driver.find_element_by_xpath("//button[@type='submit']")
     submit.click()
     time.sleep(3)
     password = context.driver.find_element_by_id("password")
     password.click()
     password.send_keys(Password)
     time.sleep(3)



@when('Click on the login button')
def clickButton(context):
    submit = context.driver.find_element_by_xpath("//button[@type='submit']")
    submit.click()



@then('user is navigate to the homepage')
def homePage(context):
    context.driver.get(r"https://www.booking.com/index.html?aid=2167732&label=37813b10aa9511ec943f05db9830e5b8")
    #context.driver.close()
    try:
        text = context.driver.find_element_by_xpath("//a[@class='bui-button bui-button--light bui-traveller-header__product-action']")

    except:

        assert False, "Test Failed"

    if text=="List your property":

        assert True, "Test Passed"



