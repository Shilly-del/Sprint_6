import pytest
import allure


from constants.constants import *
from pages.start_page import StartPage
from helpers.select_accordion_helper import select_accordion_helper

class TestHomeFaq:

    @allure.title('Проверка текста всех пунктов "Вопросов о важном"')
    @allure.description('На странице последовательно открываем все пункты аккордеона, получаем текст и сравнием его с образцом')
    @pytest.mark.parametrize("accordion_number, accordion_text, expected_text", select_accordion_helper())
    def test_home_faq(self, driver, accordion_number, accordion_text, expected_text):

        start_page = StartPage(driver)

        start_page.open_start()
        start_page.scroll_to_home_faq()
        start_page.click_accordion(accordion_number, accordion_text)

        answer = start_page.get_answer_text(accordion_text)

        assert answer == expected_text
    

