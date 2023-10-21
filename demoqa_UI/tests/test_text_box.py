import time
import pytest
from demoqa_UI.pages.text_box import TextBoxPage


@pytest.mark.usefixtures('firefox')
class TestTextboxPage:
    def test_fill_full_text_box(self):
        page = TextBoxPage(self.driver)
        page.open()
        page.maximized_window()
        page.fill_full_name_field('Viktor')
        page.fill_email_field('viktor@gmail.com')
        page.fill_current_address('Kyiv')
        page.fill_permanent_address('Lviv')
        page.click_submit_button()
        time.sleep(5)

    def test_check_fullname(self):
        name = 'Viktor'
        page = TextBoxPage(self.driver).open()
        page.maximized_window()
        page.fill_full_name_field(name)
        page.click_submit_button()
        assert name in page.get_result_fullname()

    def test_check_email(self):
        email = 'viktor@gmail.com'
        page = TextBoxPage(self.driver).open()
        page.maximized_window()
        page.fill_email_field(email)
        page.click_submit_button()
        assert email in page.get_result_email()

    def test_check_current_address(self):
        address = 'Kyiv'
        page = TextBoxPage(self.driver).open()
        page.maximized_window()
        page.fill_current_address(address)
        page.click_submit_button()
        assert address in page.get_result_current_address()

    def test_check_permanent_address(self):
        address = 'Lviv'
        page = TextBoxPage(self.driver).open()
        page.maximized_window()
        page.fill_permanent_address(address)
        page.click_submit_button()
        assert address == page.get_result_permanent_address()
