import keyring
from instagrapi import Client
self = "princejbot03"
password = "PrinceJB0t03"

global cl
cl = Client()
cl.login(self, password)

send_to = cl.user_id_from_username("princej._")
cl.direct_send(text="Message", user_ids=[send_to])

#threadlist = cl.direct_threads(2)
#for i in threadlist:
#    cl.direct_send("Hello!", [i.dict()["pk"]])