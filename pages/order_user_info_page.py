import allure

from selenium import webdriver
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.rent_info_page import RentInfoPage
from helpers.select_metro_helper import metro_locator_helper

class OrderUserInfoPage(BasePage):
        
    def __init__(self, driver):
        super().__init__(driver)
    
    def set_name(self, name):
        self.find_element(UserLocators.NAME).send_keys(name)

    def set_surname(self, surname):
        self.find_element(UserLocators.SURNAME).send_keys(surname)

    def set_address(self, address):
        self.find_element(UserLocators.ADDRESS).send_keys(address)

    def set_metro_station(self, metro_station):
        self.find_element(UserLocators.METRO_DROPDOWN).click()
        self.wait_visibility(UserLocators.METRO_LIST)
        locator = metro_locator_helper(metro_station)
        self.click(locator)
        
    def set_phone(self, phone):
        self.find_element(UserLocators.PHONE).send_keys(phone)

    @allure.step('Нажимаем "Далее"')   
    def click_order_next(self):
        self.wait.until(EC.element_to_be_clickable(UserLocators.NEXT))
        self.driver.find_element(*UserLocators.NEXT).click()
        return RentInfoPage(self.driver)

    @allure.step('Устанавливаем информацию о пользователе')
    def set_user_info(self, data):
        self.set_name(data[0])
        self.set_surname(data[1])
        self.set_address(data[2])
        self.set_metro_station(data[3])
        self.set_phone(data[4])
        return self
        
        
        

    