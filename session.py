import requests
from getpass import getpass

with requests.Session() as session:
    session.auth = ('Idosegev',getpass())

    response = session.get('https://api.github.com/user')
    response2 = session.get('https://api.github.com/user/repos')

print(response2.json())

