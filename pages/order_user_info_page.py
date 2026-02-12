import allure

from selenium import webdriver
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from helpers.select_metro_helper import metro_locator_helper

class OrderUserInfo(BasePage):
        
    def __init__(self, driver, data):
        self.name = data[0]
        self.surname = data[1]
        self.address = data[2]
        self.metro_station = data[3]
        self.phone = data[4]
        super().__init__(driver)
    
    def set_name(self):
        self.wait.until(EC.presence_of_element_located(UserLocators.NAME))
        self.driver.find_element(*UserLocators.NAME).send_keys(self.name)

    def set_surname(self):
        self.driver.find_element(*UserLocators.SURNAME).send_keys(self.surname)

    def set_address(self):
        self.driver.find_element(*UserLocators.ADDRESS).send_keys(self.address)

    def set_metro_station(self):
        self.driver.find_element(*UserLocators.METRO_DROPDOWN).click()
        self.wait.until(EC.visibility_of_element_located(UserLocators.METRO_LIST))
        locator = metro_locator_helper(self.metro_station)
        self.driver.find_element(*locator).click()
        

    def set_phone(self):
        self.driver.find_element(*UserLocators.PHONE).send_keys(self.phone)

    @allure.step('Нажимаем "Далее"')   
    def click_order_next(self):
        self.wait.until(EC.element_to_be_clickable(UserLocators.NEXT))
        self.driver.find_element(*UserLocators.NEXT).click()

    @allure.step('Устанавливаем информацию о пользователе')
    def set_user_info(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.set_metro_station()
        self.set_phone()
        self.click_order_next()

    