from playwright.sync_api import sync_playwright

def test_ing_cookie_consent():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:  
            browser = browser_type.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.ing.pl")