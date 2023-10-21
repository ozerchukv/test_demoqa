from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from demoqa_UI.widgets.general_widgets import Button


class CheckboxPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://demoqa.com/checkbox'

    def open(self) -> 'CheckboxPage':
        self.driver.get(self.url)
        return self

    def expand_folders(self, *args) -> None:
        for elem in args:
            expanded_folder_button = Button(self.driver, (By.XPATH,
                                                          f'//label[contains(@for, "tree-node-{elem}")]//ancestor::span/button'))
            expanded_folder_button.click()

    def mark_checkbox(self, *args) -> None:
        for elem in args:
            checkboxes = self.driver.find_elements(By.XPATH,
                                                   f'//label[contains(@for, "tree-node-{elem}")]/span[contains(@class, "checkbox")]')
            for checkbox in checkboxes:
                checkbox.click()

    def maximized_window(self):
        self.driver.maximize_window()
