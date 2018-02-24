# oauth2_facebook_login
Gets OAuth2 access token from Facebook automatically from a webdriver, using [requests_oauthlib](https://github.com/requests/requests-oauthlib)

I developed this when I found that I needed to get data from Facebook API automatically, but there was always the human entry for OAuth2 flow. This library takes care of that with your selected webdriver

## Installation

```bash
pip3 install --user oauth2_facebook_login
```

## Usage

### With Default Chrome Webdriver
First, setup Chrome Webdriver so that it is in PATH, which can be done in terminal

```bash
export PATH=$PATH:/home/username/Downloads/chromedriver
```

Then in Python, run

```python
from oauth2_facebook_login import get_access_token

auth = get_access_token(
    email = "user@email.com",
    password = "password",
    client_id="1234567",
    client_secret="a1b2c3d4e5",
    scope = [
            "pages_show_list",
            "manage_pages",
            "pages_manage_instant_articles",
            "pages_manage_cta",
            "ads_management",
            "business_management"
            ]
    )

auth.access_token # Facebook access token
```

### With Custom Webdriver

```python
from oauth2_facebook_login import get_access_token
from selenium import webdriver

driver = webdriver.Chrome("/home/username/Downloads/chromedriver")

auth = get_access_token(
    email = "user@email.com",
    password = "password",
    client_id="1234567",
    client_secret="a1b2c3d4e5",
    scope = [
            "pages_show_list",
            "manage_pages",
            "pages_manage_instant_articles",
            "pages_manage_cta",
            "ads_management",
            "business_management"
            ],
    driver = driver
    )

auth.access_token # Facebook access token
```

### With Custom Webdriver Headlessly

```python
from oauth2_facebook_login import get_access_token
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')

driver = webdriver.Chrome("/home/username/Downloads/chromedriver", chrome_options = chrome_options)

auth = get_access_token(
    email = "user@email.com",
    password = "password",
    client_id="1234567",
    client_secret="a1b2c3d4e5",
    scope = [
            "pages_show_list",
            "manage_pages",
            "pages_manage_instant_articles",
            "pages_manage_cta",
            "ads_management",
            "business_management"
            ],
    driver = driver
    )

auth.access_token # Facebook access token
```


## Versions

**1.0.x**
* First Publish
