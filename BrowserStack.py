from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps = [{
    'os_version': '10',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': 'Parallel Test1',  # test name
    'build': 'browserstack-build-4'  # Your tests will be organized within this build
    },
    {
    'os_version': '10',
    'os': 'Windows',
    'browser': 'firefox',
    'browser_version': 'latest',
    'name': 'Parallel Test2',
    'build': 'browserstack-build-4'
    },
    {
    'os_version': 'Big Sur',
    'os': 'OS X',
    'browser': 'safari',
    'browser_version': 'latest',
    'name': 'Parallel Test3',
    'build': 'browserstack-build-4'
    },
    {
    'os_version': '10',
    'os': 'Windows',
    'browser': 'Edge',
    'browser_version': 'latest',
    'name': 'Parallel Test2',
    'build': 'browserstack-build-4'
    },
    {
    'os_version': 'Big Sur',
    'os': 'OS X',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': 'Parallel Test3',
    'build': 'browserstack-build-4'
}]

# run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor='https://ryanlamontagne:67pron3jbRYYyLXQBLbH@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    driver.get('https://www.browserstack.com')
    driver.set_window_size(1877, 1055)
    print(driver.title)
    driver.find_element(By.CSS_SELECTOR, '#logo > .w-svg').click()
    driver.find_elements(By.XPATH, '//header/div[1]/div[1]/nav[1]/ul[1]/li[10]/button[1]')
    driver.find_elements(By.LINK_TEXT, 'Get started free')
    print(driver.current_url)
    driver.close()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()
