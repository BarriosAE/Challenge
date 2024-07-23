from playwright.sync_api import Page
from playwright.sync_api import expect
import allure

class ProductPage:
    def __init__(self, page: Page):
        self.page = page


    def verify_stock_disponible(self):
        # Buscar el elemento que contiene el texto "Stock disponible"
        # Ajusta el selector según sea necesario
        stock_text = self.page.get_by_text("Stock disponible")
    
        # Verificar si el elemento está visible
        if stock_text.is_visible():
            expect(stock_text.get_by_text("Stock disponible")).to_be_visible()
            print("El stock está disponible y visible en la página.")
            self.take_screenshot("verify_stock_disponible")
        else:
            raise Exception("El texto 'Stock disponible' no está visible.")
               

    def take_screenshot(self, step_name: str):
        self.page.screenshot(path=f"screenshots/{step_name}.png")
        with open(f"screenshots/{step_name}.png", "rb") as image_file:
            allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)
