import pytest
import allure

from selenium import webdriver
from constants.constants import *
from constants.locators import *
from pages.start_page import StartPage
from pages.order_user_info_page import OrderUserInfoPage
from pages.rent_info_page import RentInfoPage
from pages.order_info_page import  OrderInfoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrderPositive:
    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    # @allure.title('Проверка сценария заказа верхней кнопки "Заказать"')
    # @allure.description('Проверяем появление модального окна с сообщением об успешном заказе, проверяем, что при клик по логотипу самоката открывается главная страница Самоката')
    # def test_rent_up(self):

    #     start_page = StartPage(self.driver)
    #     user_info = OrderUserInfoPage(self.driver, UserData.IVAN)
    #     rent_info = RentInfoPage(self.driver)
    #     order_info = OrderInfoPage(self.driver)
        
    #     start_page.open_start()
    #     start_page.click_rent_up()

    #     user_info.set_user_info()

    #     rent_info.set_order_info()
    #     rent_info.confirmation()
            
    #     assert rent_info.check_order_succesful_popup()

    #     rent_info.click_watch()
       
    #     order_info.click_scooter()

    #     assert self.driver.current_url == Urls.BASE

    @allure.title('Проверка сценария заказа нижней кнопки"Заказать"')
    @allure.description('Проверяем появление модального окна с сообщением об успешном заказе, проверяем, что при клик по логотипу Яндекса открывается главная страница Яндекс.Дзен')
    def test_rent_down(self):

        start_page = StartPage(self.driver)
        user_info = OrderUserInfoPage(self.driver, UserData.JOHN)
        rent_info = RentInfoPage(self.driver)
        order_info = OrderInfoPage(self.driver)
        
        start_page.open_start()
        start_page.scroll_to_rent_down()
        start_page.click_rent_down()

        user_info.set_user_info()

        rent_info.set_order_info()
        rent_info.confirmation()
            
        assert rent_info.check_order_succesful_popup()

        rent_info.click_watch()

        order_info.click_yandex_logo()
        order_info.switch_to_new_window()
                
        assert order_info.check_url() == Urls.DZEN

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

