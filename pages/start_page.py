import allure

from constants.locators import *
from constants.constants import *
from pages.base_page import BasePage
from pages.order_user_info_page import OrderUserInfoPage

class StartPage(BasePage):

    def __init__(self, driver): 
        super().__init__(driver)

    @allure.step('Открываем стартовую страницу')
    def open_start(self):
        self.open(Urls.BASE)
        return self

    @allure.step('Крутим до вопросов о важном')           
    def scroll_to_home_faq(self):
        self.scroll_to_element(BaseLocators.HOME_FAQ)
        return self
                
    @allure.step('Открываем аккордеон, за один прогон - один пункт')   
    def click_accordion(self, question, answer):
        element = self.find_element(question)
        self.execute_click(question)
        self.wait_visibility(answer)
        return self

    @allure.step('Получаем текст ответа')     
    def get_answer_text(self, answer):
        return self.get_text(answer)

    @allure.step('Нажимаем "Заказать"') 
    def click_rent_up(self):
        self.wait_clickable(BaseLocators.RENT_UP)
        self.click(BaseLocators.RENT_UP)
        return OrderUserInfoPage(self.driver)

    @allure.step('Крутим до нижней кнопки "Заказать"') 
    def scroll_to_rent_down(self):
        self.scroll_to_element(BaseLocators.RENT_DOWN)
        return self
    
    @allure.step('Нажимаем "Заказать"') 
    def click_rent_down(self):
        self.wait_clickable(BaseLocators.RENT_DOWN)
        self.click(BaseLocators.RENT_DOWN)
        return OrderUserInfoPage(self.driver)
    


        