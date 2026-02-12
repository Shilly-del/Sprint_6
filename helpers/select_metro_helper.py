from selenium.webdriver.common.by import By

def metro_locator_helper(metro_station):

    locator = (By.XPATH, f'//*[@class="Order_Text__2broi" and text() = "{metro_station}"]')
    return locator