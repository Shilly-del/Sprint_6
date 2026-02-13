import pytest

from selenium import webdriver

# Фикстура драйвера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


