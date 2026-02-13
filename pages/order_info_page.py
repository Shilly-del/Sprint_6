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
        self.driver.find_element(*BaseLocators.SCOOTER).click()
        self.wait.until(EC.presence_of_element_located(BaseLocators.HEADER))

    @allure.step('Кликаем по логотипу Яндекса') 
    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.LOGO))
        self.driver.find_element(*BaseLocators.LOGO).click()

    

