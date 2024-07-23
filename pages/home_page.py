from playwright.sync_api import Page
import allure

class HomePage:
    URL = "https://www.mercadolibre.com.ar/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        self.take_screenshot("home_page")

    def click_mas_tarde(self):
        self.page.get_by_role("button", name="Más tarde").click()
        self.take_screenshot("click_mas_tarde")

    def search_product(self, product: str):
        self.page.get_by_placeholder("Buscar productos, marcas y má").click()
        self.page.get_by_placeholder("Buscar productos, marcas y má").fill(product)
        self.page.get_by_placeholder("Buscar productos, marcas y má").press("Enter")
        self.take_screenshot("search_product")

    def take_screenshot(self, step_name: str):
        self.page.screenshot(path=f"screenshots/{step_name}.png")
        with open(f"screenshots/{step_name}.png", "rb") as image_file:
            allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)
