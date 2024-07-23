import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

@pytest.mark.regression

def test_search_battery(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_mas_tarde()
    home_page.search_product("Bateria 12v")

    search_results_page = SearchResultsPage(page)
    search_results_page.click_first_result()

    product_page = ProductPage(page)
    product_page.verify_stock_disponible()
