import keyring
from instagrapi import Client
self = "princejbot03"
password = keyring.get_password("instagramBot1", self)

global cl
cl = Client()
cl.login(self, password)
