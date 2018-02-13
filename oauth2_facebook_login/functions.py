from selenium import webdriver
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix

def get_access_token(email, password, client_id = "", client_secret = "", scope = [], driver = None):
    """
    Logins to Facebook and get token for OAuth2

    Parameters
    ----------
    email: string
        login email for OAuth2 account
    password: string
        login password for OAuth2 account
    client_id: string
        App client id, taken from a specific app from https://developers.facebook.com/apps/
    client_secret: string
        App client secret, taken from a specific app from https://developers.facebook.com/apps/
    scope: list
        A list of OAuth2 scope desired for this app. For example,
        scope = [
                "pages_show_list",
                "manage_pages",
                "pages_manage_instant_articles",
                "pages_manage_cta",
                "ads_management",
                "business_management"
                ]
    driver: selenium.webdriver (optional)
        Selenium webdriver used for login. Chrome is default, but its location has to be specified in PATH

    Output
    ------
    requests_oauthlib.OAuth2Session

    """

    authorization_base_url = 'https://www.facebook.com/dialog/oauth'
    token_url = 'https://graph.facebook.com/oauth/access_token'
    redirect_uri = 'https://localhost/'     # Should match Site URL

    if driver == None:
        driver = webdriver.Chrome()

    facebook = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    facebook = facebook_compliance_fix(facebook)

    authorization_url, state = facebook.authorization_url(authorization_base_url)
    driver.get(authorization_url)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginbutton").click()
    redirect_response = driver.current_url

    facebook.fetch_token(token_url, client_secret=client_secret,
    authorization_response=redirect_response)

    driver.close()
    return facebook
