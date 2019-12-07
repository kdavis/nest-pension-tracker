import requests
import re


class NestPension():
    LOGIN_FORM = "https://www.nestpensions.org.uk/pkmslogin.form"
    LOGIN_REDIRECT = "https://www.nestpensions.org.uk/schemeweb/NestWeb/faces/secure/common/pages/loginResolver.xhtml"
    FUND_URL = "https://www.nestpensions.org.uk/schemeweb/NestWeb/faces/secure/FE/pages/fundValueLanding.xhtml"
    LOGIN_SUCCESS = False

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.session()

    def login(self):
        login_attempt = self.session.post(self.LOGIN_FORM, data={
            "username": self.username,
            "password": self.password,
            "login-form-type": "pwd"
        }, allow_redirects=False)
        if "location" not in login_attempt.headers:
            return
        if login_attempt.headers["location"] == self.LOGIN_REDIRECT:
            self.LOGIN_SUCCESS = True

        self.session.get(self.LOGIN_REDIRECT)

    def get_value(self):
        fund_data = self.session.get(self.FUND_URL)

        matches = re.search(
            "£([0-9]+\.[0-9]{2})", fund_data.content.decode('utf-8'), re.M)

        if matches:
            return matches.group(1)

        return None

    def is_logged_in(self):
        return self.LOGIN_SUCCESS
