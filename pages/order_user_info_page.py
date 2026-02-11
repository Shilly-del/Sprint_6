import allure

from selenium import webdriver
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderUserInfo():
        
    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.name = data[0]
        self.surname = data[1]
        self.address = data[2]
        self.phone = data[3]
    
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
        self.driver.find_element(*UserLocators.METRO_STATION).click()

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

    