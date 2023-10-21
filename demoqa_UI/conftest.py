import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def firefox(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def chrome(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
