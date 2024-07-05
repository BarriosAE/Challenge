import pytest
from pages.home_page import HomePage
from playwright.sync_api import Page
from pages.search_results_page import SearchResultsPage

def test_aliexpress(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_no_permitir()
    home_page.search("instax mini")

    search_results_page = SearchResultsPage(page)
    page1 = search_results_page.click_report_fraud_item()
    search_results_page = SearchResultsPage(page1)
    search_results_page.verify_extra_discount()
