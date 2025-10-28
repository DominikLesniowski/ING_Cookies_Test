import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from pages.cookie_page.ing_cookie_page import IngCookiePage

def test_ing_cookie_consent():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:  
            browser = browser_type.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            cookie_page = IngCookiePage(page)
 
            cookie_page.open_url()
            cookie_page.customize_cookies_button()
            cookie_page.switch_toggle_analytics_cookies()
            #asercja czy jest zaznaczone 
            cookie_page.accept_selected()
            #upewnic sie , ze modal zniknal 
            cookies = cookie_page.get_all_cookies(context)
        
           
            session_cookie_policyGDPR_details = cookie_page.get_cookie_by_name(cookies, "cookiePolicyGDPR__details")
            session_cookie_policyGDPR = cookie_page.get_cookie_by_name(cookies, "cookiePolicyGDPR")
            
            assert session_cookie_policyGDPR_details["name"] == "cookiePolicyGDPR__details", "Cookie name: 'cookiePolicyGDPR__details' ma niepoprawną wartość!"
            assert session_cookie_policyGDPR["name"] == "cookiePolicyGDPR", "Cookie name: 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert session_cookie_policyGDPR["value"] == "3", "Cookie 'cookiePolicyGDPR' ma niepoprawną wartość!"
            assert "cookieCreateTimestamp" in session_cookie_policyGDPR_details["value"], "Cookie 'cookiePolicyGDPR__details' ma niepoprawną wartość!"

            browser.close()
