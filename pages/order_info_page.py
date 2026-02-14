import allure

from constants.locators import *
from constants.constants import *
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
    

