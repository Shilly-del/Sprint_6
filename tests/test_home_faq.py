import pytest
import allure

from selenium import webdriver
from constants.constants import *
from constants.locators import *
from pages.start_page import StartPage


class TestHomeFaq:
    driver = None
    sets = [(BaseLocators.Q0, BaseLocators.A0, Answers.AN0),
            (BaseLocators.Q1, BaseLocators.A1, Answers.AN1),
            (BaseLocators.Q2, BaseLocators.A2, Answers.AN2),
            (BaseLocators.Q3, BaseLocators.A3, Answers.AN3),
            (BaseLocators.Q4, BaseLocators.A4, Answers.AN4),
            (BaseLocators.Q5, BaseLocators.A5, Answers.AN5),
            (BaseLocators.Q6, BaseLocators.A6, Answers.AN6),
            (BaseLocators.Q7, BaseLocators.A7, Answers.AN7)
            ]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка текста всех пунктов "Вопросов о важном"')
    @allure.description('На странице последовательно открываем все пункты аккордеона, получаем текст и сравнием его с образцом')
    @pytest.mark.parametrize("accordion_number, accordion_text, expected_text", sets)
    def test_home_faq(self, accordion_number, accordion_text, expected_text):

        start_page = StartPage(self.driver)
        start_page.open_start() 
        start_page.scroll_to_home_faq()
        start_page.click_accordion(accordion_number, accordion_text)
        answer = start_page.get_answer_text(accordion_text)

        assert answer == expected_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

