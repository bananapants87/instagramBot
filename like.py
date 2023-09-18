import time, login
cl = login.cl

def likeAll(medias):
    counter = 0
    for i in medias:
        media_item = i.dict()
        pk = media_item["pk"]
        pk = i.dict()["pk"]
        cl.media_like(pk)
        counter += 1
        print(f"Liked Picture {counter}")
        time.sleep(3)
    
    return

def likeSingle(pk):
    cl.media_like(pk)
    return