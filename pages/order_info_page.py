import time
import allure

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderInfo():
    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Кликаем по логотипу Самоката') 
    def click_scooter(self):
        self.driver.find_element(*BaseLocators.SCOOTER).click()
        self.wait.until(EC.presence_of_element_located(BaseLocators.HEADER))

    @allure.step('Кликаем по логотипу Яндекса') 
    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.LOGO))
        self.driver.find_element(*BaseLocators.LOGO).click()

    @allure.step('Переключаемся на новую вкладку')            
    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        time.sleep(5)

    @allure.step('Получаем адрес страницы')
    def check_url(self):
        return self.driver.current_url

