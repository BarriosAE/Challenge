import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from playwright.sync_api import expect

@pytest.mark.regression

def test_search_battery(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    ## Verificar que el texto "Elegí cómo pagar" esté visible
    expect(page.get_by_text("Elegí cómo pagar")).to_be_visible()
    home_page.click_mas_tarde()
    ## Ingresar "Bateria 12v" en el campo de búsqueda
    home_page.search_product("Bateria 12v")
    ## Hacer clic en el botón de búsqueda
    search_results_page = SearchResultsPage(page)
    ## Hacer clic en el primer resultado
    search_results_page.click_first_result()

    ## Ingresamos al producto
    product_page = ProductPage(page)
    ## Verificar que el stock esté disponible
    product_page.verify_stock_disponible()
    ## Verificar que el texto "Stock disponible" esté visible
    expect(page.get_by_text("Stock disponible")).to_be_visible()
