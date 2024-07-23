from playwright.sync_api import Page
import allure

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_first_result(self):
        self.page.locator("li").filter(has_text="Bateria Alarma 12v 7ah 7a Recargable Leds Ups Garantia 1 Año$35.527en 6 cuotas").get_by_role("link").click()
        self.take_screenshot("click_first_result")

    def take_screenshot(self, step_name: str):
        self.page.screenshot(path=f"screenshots/{step_name}.png")
        with open(f"screenshots/{step_name}.png", "rb") as image_file:
            allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)
