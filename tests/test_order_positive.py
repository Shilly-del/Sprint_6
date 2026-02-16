import allure

from constants.constants import *
from pages.start_page import StartPage

class TestOrderPositive:
        
    @allure.title('Проверка сценария заказа верхней кнопки "Заказать"')
    @allure.description('Проверяем появление модального окна с сообщением об успешном заказе')
    def test_rent_up(self, driver):

        start_page = StartPage(driver)
        
        user_info = start_page.open_start()
        
        rent_info = user_info.click_rent_up().set_user_info(UserData.IVAN).click_order_next()

        rent_info.set_order_info().confirmation()
         
        assert rent_info.check_order_succesful_popup()

    @allure.title('Проверка клика по логотипу Самоката после заказа')
    @allure.description('Проверяем переход на главную страницу Самоката при клике по логотипу Самоката после успешного заказа')
    def test_rent_logo_scooter(self, driver):

        start_page = StartPage(driver)
                
        user_info = start_page.open_start()

        rent_info = user_info.click_rent_up().set_user_info(UserData.IVAN).click_order_next()

        order_info = rent_info.set_order_info().confirmation().click_watch()

        order_info.wait_invert().click_scooter()

        assert order_info.check_url() == Urls.BASE

    @allure.title('Проверка сценария заказа нижней кнопки"Заказать"')
    @allure.description('Проверяем появление модального окна с сообщением об успешном заказе')
    def test_rent_down(self, driver):

        start_page = StartPage(driver)
                
        user_info = start_page.open_start()

        rent_info = user_info.scroll_to_rent_down().click_rent_down().set_user_info(UserData.JOHN).click_order_next()

        rent_info.set_order_info().confirmation()
         
        assert rent_info.check_order_succesful_popup()

    @allure.title('Проверка клика по логотипу Яндекса после заказа')
    @allure.description('Проверяем открытие через редирект в новой вкладке главной страницы Яндекс.Дзен при клике по логотипу Яндекса после успешного заказа')
    def test_rent_logo_yandex(self, driver):

        start_page = StartPage(driver)
                
        user_info = start_page.open_start()

        rent_info = user_info.scroll_to_rent_down().click_rent_down().set_user_info(UserData.JOHN).click_order_next()

        order_info = rent_info.set_order_info().confirmation().click_watch()

        order_info.wait_invert().click_yandex_logo().switch_to_new_window()

        assert order_info.check_dzen()

   

