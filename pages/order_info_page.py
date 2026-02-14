import allure

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderInfoPage(BasePage):

    def __init__(self, driver): 
        super().__init__(driver)

    @allure.step('Кликаем по логотипу Самоката') 
    def click_scooter(self):
        self.wait_clickable(BaseLocators.SCOOTER)
        self.click(BaseLocators.SCOOTER)
        return self

    @allure.step('Кликаем по логотипу Яндекса') 
    def click_yandex_logo(self):
        self.wait_clickable(BaseLocators.LOGO)
        self.click(BaseLocators.LOGO)
        return self
    

