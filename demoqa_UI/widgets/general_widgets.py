from abc import ABC

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class Component(ABC):
    def __init__(self, driver: WebDriver = None, locator: tuple = None) -> None:
        if driver:
            self.driver: WebDriver = driver
            if locator:
                self.locator = locator
                self.element: WebElement = self.driver.find_element(*self.locator)
        self._actions = ActionChains(driver=driver)

    def type_of(self) -> str:
        return self.__class__.__name__

    def scroll_to(self) -> None:
        self._actions.scroll_to_element(self.element)

    def scroll_into_view(self) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)


class Button(Component):
    def __init__(self, driver: WebDriver = None, locator: tuple = None):
        super().__init__(driver=driver, locator=locator)
        self._actions: ActionChains = self._actions

    def hover(self):
        self._actions.move_to_element(self.element).perform()

    def click(self):
        self.element.click()

    def doubleclick(self):
        self._actions.double_click(self.element).perform()

    def right_click(self):
        self._actions.context_click(self.element).perform()

    def get_attribute(self, attr):
        return self.element.get_attribute(attr)




