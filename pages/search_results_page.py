from playwright.sync_api import Page, expect

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_report_fraud_item(self):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name="Report fraud item Fujifilm-impresora Instax Mini Link 2 Original, dispositivo").click()
        return page1_info.value

    def verify_extra_discount(self):
        expect(self.page.get_by_text("+2 unidades").first).to_be_visible()