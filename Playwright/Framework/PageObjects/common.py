class Common:
    def __init__(self, playwright):
        self.playwright = playwright

    # methods
    def create_browser_context(self, browser_type, headless_mode):

        if headless_mode == "True" or headless_mode == "true" or headless_mode == "TRUE":
            headless = True
            if browser_type == "chromium" or browser_type == "chrome" or browser_type == "Chromium" or browser_type == "Chrome" or browser_type == "CHROMIUM" or browser_type == "CHROME":
                browser = self.playwright.chromium.launch(headless=True)
            elif browser_type == "firefox" or browser_type == "Firefox" or browser_type == "FIREFOX":
                browser = self.playwright.firefox.launch(headless=True)
            elif browser_type == "webkit" or browser_type == "Webkit" or browser_type == "WEBKIT":
                browser = self.playwright.webkit.launch(headless=True)
        else:
            headless = False
            if browser_type == "chromium" or browser_type == "chrome" or browser_type == "Chromium" or browser_type == "Chrome" or browser_type == "CHROMIUM" or browser_type == "CHROME":
                browser = self.playwright.chromium.launch(headless=False)
            elif browser_type == "firefox" or browser_type == "Firefox" or browser_type == "FIREFOX":
                browser = self.playwright.firefox.launch(headless=False)
            elif browser_type == "webkit" or browser_type == "Webkit" or browser_type == "WEBKIT":
                browser = self.playwright.webkit.launch(headless=False)
        context = browser.new_context()
        return context.new_page()
