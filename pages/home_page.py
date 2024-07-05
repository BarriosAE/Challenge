from playwright.sync_api import Page

class HomePage:
    URL = "https://es.aliexpress.com/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def click_no_permitir(self):
        self.page.locator('div.Sk1_X._1-SOk').click()

    def search(self, text: str):
        self.page.get_by_placeholder("auriculares a bluetooth").fill(text)
        self.page.locator('input[type="button"]').click()
