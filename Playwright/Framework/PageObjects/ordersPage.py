class OrdersPage:
    def __init__(self, page):
        self.page = page

    # methods
    def clickViewByOrderId(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()

