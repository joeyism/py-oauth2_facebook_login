from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('oauth2_facebook_login/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'oauth2_facebook_login',
        packages = ['oauth2_facebook_login'], # this must be the same as the name above
        version = version,
        description = 'Returns Facebook OAuth2 access token',
        author = 'Joey Sham',
        author_email = 'sham.joey@gmail.com',
        url = 'https://github.com/joeyism/oauth2_facebook_login', # use the URL to the github repo
        download_url = 'https://github.com/joeyism/oauth2_facebook_login/dist/' + version + '.tar.gz',
        keywords = ['oauth2', 'facebook', 'login'], 
        classifiers = [],
        install_requires=["selenium", "requests_oauthlib"],
        )
