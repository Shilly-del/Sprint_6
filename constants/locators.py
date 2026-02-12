from selenium.webdriver.common.by import By

class BaseLocators:

    HOME_FAQ = (By.CLASS_NAME, "Home_SubHeader__zwi_E")
    RENT_UP = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g"]')
    SCOOTER = (By.XPATH, '//img[@alt="Scooter"]')
    LOGO = (By.XPATH, '//img[@alt="Yandex"]')
    HEADER = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    RENT_DOWN = (By.CSS_SELECTOR, '[class = "Button_Button__ra12g Button_Middle__1CSJM"]')
    
    
    Q0 = (By.XPATH, '//*[@aria-controls="accordion__panel-0"]')
    Q1 = (By.XPATH, '//*[@aria-controls="accordion__panel-1"]')
    Q2 = (By.XPATH, '//*[@aria-controls="accordion__panel-2"]')
    Q3 = (By.XPATH, '//*[@aria-controls="accordion__panel-3"]')
    Q4 = (By.XPATH, '//*[@aria-controls="accordion__panel-4"]')
    Q5 = (By.XPATH, '//*[@aria-controls="accordion__panel-5"]')
    Q6 = (By.XPATH, '//*[@aria-controls="accordion__panel-6"]')
    Q7 = (By.XPATH, '//*[@aria-controls="accordion__panel-7"]')

    A0 = (By.ID, 'accordion__panel-0')
    A1 = (By.ID, 'accordion__panel-1')
    A2 = (By.ID, 'accordion__panel-2')
    A3 = (By.ID, 'accordion__panel-3')
    A4 = (By.ID, 'accordion__panel-4')
    A5 = (By.ID, 'accordion__panel-5')
    A6 = (By.ID, 'accordion__panel-6')
    A7 = (By.ID, 'accordion__panel-7')

class UserLocators:
    NAME = (By.XPATH, '//*[@placeholder="* Имя"]')
    SURNAME = (By.XPATH, '//*[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_DROPDOWN = (By.XPATH, '//*[@class="select-search__input"]')
    PHONE = (By.XPATH, '//*[@wfd-id="id5"]')
    METRO_LIST = (By.XPATH, '//*[@class="select-search__select"]')
    NEXT = (By.XPATH, '//div[@class = "Order_NextButton__1_rCA"]/button[text() = "Далее"]')

class RentLocators:
    DATE = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]')
    PERIOD = (By.XPATH, '//*[@class="Dropdown-arrow"]')
    PERIOD_5DAYS = (By.XPATH, '//*[@class="Dropdown-option" and text() = "пятеро суток"]')
    ORDER = (By.XPATH, '//*[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]')
    CONFIRM = (By.XPATH, '//*[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Да"]')
    WATCH = (By.XPATH, '//*[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]')
    MODAL = (By.XPATH, '//*[@class="Order_Modal__YZ-d3"]')
    
class Dzenlocators:
    DZEN_HEADER = (By.XPATH, '//header[@id="dzen-header"]')

class MetroStation:
    ROKOSSOVSKY_BOULEVARD = (By.XPATH, '//*[@class="Order_Text__2broi" and text() = "Бульвар Рокоссовского"]')
    CHERKIZOVSKAYA = (By.XPATH, '//*[@class="Order_Text__2broi" and text() = "Черкизовская"]')

