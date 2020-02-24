import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Impelements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self,r):
        """Attach an API  to custom auth header"""
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r

response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345-token'))
print(TokenAuth('12345-token').__call__(response).json())