import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import page

from Playwright.Framework.PageObjects.common import Common
from Playwright.Framework.PageObjects.loginPage import LoginPage
from utils.apiBase import APIUtils

with open("Playwright/Framework/Data/credentials.json") as f:
    test_data = json.load(f)
    test_credentials = test_data["credentials"]
print(f"Test data loaded from json file: {test_data}")


@pytest.mark.parametrize("test_credentials_list", test_credentials)
def test_e2eTest_createOrderAndVerify(playwright: Playwright, test_credentials_list, page):
    # here we will create order by API call
    orderId = APIUtils.createOrder(playwright, userCredentials=test_credentials_list)

    # here we will verify orderId in UI
    common = Common(playwright)
    page = common.create_browser_context("chrome", "False")
    loginPage = LoginPage(page)
    loginPage.navigate()
    dashboardPage = loginPage.login(test_credentials_list)
    orderDetailsPage = dashboardPage.click_order_button()
    orderDetailsPage.clickViewByOrderId(orderId)

    # here we will add assertion to verify orderId in UI
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
