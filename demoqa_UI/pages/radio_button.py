from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from demoqa_UI.widgets.general_widgets import Button


class RadioButtonPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://demoqa.com/radio-button'

    def open(self) -> 'RadioButtonPage':
        self.driver.get(self.url)
        return self

    def activate_yes_button(self, name):
        yes_button = Button(self.driver, (By.XPATH,
                                          f'//label[contains(@for, "{name}Radio")]'))
        Button.click(yes_button)

    def button_is_active(self, name) -> bool:
        element = self.driver.find_element(By.XPATH,
                                           f'//label[contains(@for, "{name}Radio")]//ancestor::div[contains(@class, "radio")]/input')
        return element.is_selected()

    def maximized_window(self):
        self.driver.maximize_window()
