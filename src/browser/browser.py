from playwright.sync_api import sync_playwright, TimeoutError

class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        chromium = self.playwright.chromium
        self.browser = chromium.launch()
        self.page = self.browser.new_page()

    def new_page(self):
        return self.browser.new_page()
    
    def go_to(self, url):
        try:
            self.page.goto(url, timeout=30000)
        except TimeoutError as e:
            print(f"TimeoutError: {e} when trying to navigate to {url}")
            return False
        return True