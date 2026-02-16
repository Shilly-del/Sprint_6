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
        
    @allure.step('Кликаем по логотипу Яндекса') 
    def click_yandex_logo(self):
        self.wait_clickable(BaseLocators.LOGO)
        self.click(BaseLocators.LOGO)
            
    def wait_invert(self):
        self.find_element(RentLocators.INVERT)
        return self

    def check_dzen(self):
        self.check_new_url(Urls.DZEN)
        return self