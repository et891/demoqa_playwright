from playwright.sync_api import Page

class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements_button = page.get_by_role("heading",name="Elements")
        self.forms_button = page.locator("#userEmail")
        self.alerts_frame_windows_button = page.locator("#currentAddress")
        self.widgets_button = page.locator("#permanentAddress")
        self.interaction_button = page.locator("#submit")



    def goto_elements(self):
        self.elements_button.click()


