import allure

from selenium import webdriver
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from pages.base_page import BasePage

class RentInfoPage(BasePage):

    def __init__(self, driver): 
        super().__init__(driver)
    
    @allure.step('Устанавливаем дату')
    def set_date(self):
        date = (datetime.now() + timedelta(days=3)).strftime('%d.%m.%Y')
        self.find_element(RentLocators.DATE).send_keys(date)

    @allure.step('Устанавливаем срок аренды')
    def set_rent_period(self):
        self.click(RentLocators.PERIOD)
        self.wait_visibility(RentLocators.PERIOD_5DAYS)
        self.click(RentLocators.PERIOD_5DAYS)

    @allure.step('Кликаем "Далее"')
    def click_order_next(self):
        self.wait_clickable(RentLocators.ORDER)
        self.click(RentLocators.ORDER)

    @allure.step('Нажимаем "ДА"')
    def confirmation(self):
        self.wait_clickable(RentLocators.CONFIRM)
        self.click(RentLocators.CONFIRM)

    @allure.step('Кликаем "Посмотреть статус"')
    def click_watch(self):
        self.wait_clickable(RentLocators.WATCH)
        self.click(RentLocators.WATCH)

    @allure.step('Устанавливаем информацию об аренде')
    def set_order_info(self):
        self.set_date()
        self.set_rent_period()
        self.click_order_next()
        return self

    @allure.step('Проверяем появление модального окна')
    def check_order_succesful_popup(self):
        return self.find_element(RentLocators.MODAL)
    