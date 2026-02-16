import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():

    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def execute_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def action_click(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        return self.find_element(locator).text

    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        time.sleep(5)
    
    def check_url(self):
        return self.driver.current_url
