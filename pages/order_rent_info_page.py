import allure

from selenium import webdriver
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class OrderRentInfo():
        
    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step('Устанавливаем дату')
    def set_date(self):
        self.wait.until(EC.presence_of_element_located(RentLocators.DATE))
        date = (datetime.now() + timedelta(days=3)).strftime('%d.%m.%Y')
        self.driver.find_element(*RentLocators.DATE).send_keys(date)

    @allure.step('Устанавливаем срок аренды')
    def set_rent_period(self):
        self.driver.find_element(*RentLocators.PERIOD).click()
        self.wait.until(EC.visibility_of_element_located(RentLocators.PERIOD_5DAYS))
        self.driver.find_element(*RentLocators.PERIOD_5DAYS).click()

    @allure.step('Кликаем "Далее"')
    def click_order_next(self):
        self.wait.until(EC.element_to_be_clickable(RentLocators.ORDER))
        self.driver.find_element(*RentLocators.ORDER).click()

    @allure.step('Нажимаем "ДА"')
    def confirmation(self):
        self.wait.until(EC.element_to_be_clickable(RentLocators.CONFIRM))
        self.driver.find_element(*RentLocators.CONFIRM).click()

    @allure.step('Кликаем "Посмотреть статус"')
    def click_watch(self):
        self.wait.until(EC.element_to_be_clickable(RentLocators.WATCH))
        self.driver.find_element(*RentLocators.WATCH).click()

    @allure.step('Устанавливаем информацию об аренде')
    def set_order_info(self):
        self.set_date()
        self.set_rent_period()
        self.click_order_next()

    @allure.step('Проверяем появление модального окна')
    def check_order_succesful_popup(self):
        return self.wait.until(EC.presence_of_element_located(RentLocators.MODAL))
    