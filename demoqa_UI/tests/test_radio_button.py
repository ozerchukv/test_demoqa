import time
import pytest
from demoqa_UI.pages.radio_button import RadioButtonPage


@pytest.mark.usefixtures('firefox')
class TestRadiobuttonPage:
    def test_activate_yes_button(self):
        page = RadioButtonPage(self.driver)
        page.open()
        page.maximized_window()
        page.activate_yes_button('yes')
        time.sleep(5)




