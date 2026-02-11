import allure

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from constants.locators import *
from constants.constants import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
        
    def __init__(self, driver): 
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Крутим до вопросов о важном')           
    def scroll_to_home_faq(self):
        element = self.driver.find_element(*BaseLocators.HOME_FAQ)
        ActionChains(self.driver).move_to_element(element).perform()
        
    @allure.step('Открываем аккордеон, за один прогон - один пункт')   
    def click_accordion(self, question, answer):
        element = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.visibility_of_element_located(answer))

    @allure.step('Получаем текст ответа')     
    def get_answer_text(self, answer):
        answer = self.driver.find_element(*answer).text
        return answer

    @allure.step('Нажимаем "Заказать"') 
    def click_rent_up(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.RENT_UP))
        self.driver.find_element(*BaseLocators.RENT_UP).click()

    @allure.step('Крутим до нижней кнопки "Заказать"') 
    def scroll_to_rent_down(self):
        self.wait.until(EC.presence_of_element_located(BaseLocators.RENT_DOWN))
        element = self.driver.find_element(*BaseLocators.RENT_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step('Нажимаем "Заказать"') 
    def click_rent_down(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.RENT_DOWN))
        self.driver.find_element(*BaseLocators.RENT_DOWN).click()