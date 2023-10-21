import time
import pytest
from demoqa_UI.pages.check_box import CheckboxPage

expand_list = ['home', 'desktop', 'documents', 'office', 'downloads']
marked_list = ['commands', 'general']


@pytest.mark.usefixtures('firefox')
class TestCheckBoxPage:

    def test_checkboxes(self):
        page = CheckboxPage(self.driver)
        page.open()
        page.maximized_window()
        page.expand_folders(*expand_list)
        page.mark_checkbox(*marked_list)
        time.sleep(5)










