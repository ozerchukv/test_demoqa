from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://demoqa.com/text-box'
        self.driver = driver
        self.full_name_field = (By.ID, 'userName')
        self.email_field = (By.ID, 'userEmail')
        self.current_address = (By.CSS_SELECTOR, 'textarea#currentAddress')
        self.permanent_address = (By.CSS_SELECTOR, 'textarea#permanentAddress')
        self.submit_button = (By.ID, 'submit')
        self.result_fullname = (By.ID, 'name')
        self.result_email = (By.ID, 'email')
        self.result_current_address = (By.CSS_SELECTOR, 'p#currentAddress')
        self.result_permanent_address = (By.CSS_SELECTOR, 'p#permanentAddress')

    def open(self) -> 'TextBoxPage':
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    def clear_email_field(self) -> None:
        self.driver.find_element(*self.email_field).clear()

    def fill_email_field(self, text: str, clear=False) -> None:
        if clear:
            self.clear_email_field()
        self.driver.find_element(*self.email_field).send_keys(text)

    def get_email_field_element(self) -> WebElement:
        return self.driver.find_element(*self.email_field)

    def clear_current_address(self) -> None:
        self.driver.find_element(*self.current_address).clear()

    def fill_current_address(self, text: str) -> None:
        self.driver.find_element(*self.current_address).send_keys(text)

    def clear_permanent_address(self) -> None:
        self.driver.find_element(*self.permanent_address).clear()

    def fill_permanent_address(self, text: str) -> None:
        self.driver.find_element(*self.permanent_address).send_keys(text)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def get_result_fullname(self):
        return self.driver.find_element(*self.result_fullname).text

    def get_result_email(self):
        return self.driver.find_element(*self.result_email).text

    def get_result_current_address(self):
        return self.driver.find_element(*self.result_current_address).text

    def get_result_permanent_address(self):
        permanent_address = self.driver.find_element(*self.result_permanent_address).text
        return permanent_address.split(':')[-1]

    def maximized_window(self):
        self.driver.maximize_window()
