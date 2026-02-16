import allure

from constants.constants import *
from pages import StartPage, OrderUserInfoPage, RentInfoPage, OrderInfoPage

class TestOrderPositive:
        
    @allure.title('Проверка сценария заказа верхней кнопки "Заказать"')
    @allure.description('Проверяем появление модального окна с сообщением об успешном заказе')
    def test_rent_up(self, driver):

        start_page = StartPage(driver)
        start_page.open_start().click_rent_up()

        user_info = OrderUserInfoPage(driver)
        user_info.set_user_info(UserData.IVAN).click_order_next()

        rent_info = RentInfoPage(driver)
        rent_info.set_order_info().confirmation()
         
        assert rent_info.check_order_succesful_popup()

    @allure.title('Проверка клика по логотипу Самоката после заказа')
    @allure.description('Проверяем переход на главную страницу Самоката при клике по логотипу Самоката после успешного заказа')
    def test_rent_logo_scooter(self, driver):

        start_page = StartPage(driver)
        start_page.open_start().click_rent_up()

        user_info = OrderUserInfoPage(driver)
        user_info.set_user_info(UserData.IVAN).click_order_next()

        rent_info = RentInfoPage(driver)
        rent_info.set_order_info().confirmation().click_watch()

        order_info = OrderInfoPage(driver)
        order_info.wait_invert().click_scooter()

        assert order_info.check_url() == Urls.BASE

    @allure.title('Проверка сценария заказа нижней кнопки"Заказать"')
    @allure.description('Проверяем появление модального окна с сообщением об успешном заказе')
    def test_rent_down(self, driver):

        start_page = StartPage(driver)
        start_page.open_start().scroll_to_rent_down().click_rent_down()
                
        user_info = OrderUserInfoPage(driver)
        user_info.set_user_info(UserData.JOHN).click_order_next()

        rent_info = RentInfoPage(driver)
        rent_info.set_order_info().confirmation()
         
        assert rent_info.check_order_succesful_popup()

    @allure.title('Проверка клика по логотипу Яндекса после заказа')
    @allure.description('Проверяем открытие через редирект в новой вкладке главной страницы Яндекс.Дзен при клике по логотипу Яндекса после успешного заказа')
    def test_rent_logo_yandex(self, driver):

        start_page = StartPage(driver)
        start_page.open_start().scroll_to_rent_down().click_rent_down()
                
        user_info = OrderUserInfoPage(driver)
        user_info.set_user_info(UserData.JOHN).click_order_next()

        rent_info = RentInfoPage(driver)
        rent_info.set_order_info().confirmation().click_watch()

        order_info = OrderInfoPage(driver)
        order_info.wait_invert().click_yandex_logo()
        order_info.switch_to_new_window()

        assert order_info.check_dzen()

   

