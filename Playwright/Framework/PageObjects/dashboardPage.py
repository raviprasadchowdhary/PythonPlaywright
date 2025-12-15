from Playwright.Framework.PageObjects.ordersPage import OrdersPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    # methods
    def click_order_button(self):
        OrderButton = self.page.get_by_role("button", name="Orders")
        OrderButton.click()
        return OrdersPage(self.page)