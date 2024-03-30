from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        chromium = self.playwright.chromium
        self.browser = chromium.launch()
        self.page = self.browser.new_page()

    def new_page(self):
        return self.browser.new_page()