from playwright.sync_api import sync_playwright
from ing_cookie_page import IngCookiePage


def test_ing_cookie_consent():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:  
            browser = browser_type.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            cookie_page = IngCookiePage(page)
 
            cookie_page.open()
            cookie_page.customize_cookies()
            cookie_page.toggle_analytics_cookies()
            cookie_page.accept_selected()
            cookies = cookie_page.get_all_cookies(context)
        

            session_cookie = cookie_page.get_cookie_by_name(cookies, "cookiePolicyGDPR__details")
            session_cookie2 = cookie_page.get_cookie_by_name(cookies, "cookiePolicyGDPR")
            
            assert session_cookie["name"] == "cookiePolicyGDPR__details", "Cookie name: 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
            assert session_cookie2["name"] == "cookiePolicyGDPR", "Cookie name: 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert session_cookie2["value"] == "3", "Cookie 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert "cookieCreateTimestamp" in session_cookie["value"], "Cookie 'cookiePolicyGDPR__details' ma niepoprawną wartość!"

            browser.close()
