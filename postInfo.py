import userID, emoji

def grabCaptions(medias): #grabs captions from the users' posts
    file = open("text.txt", "w")
    for i in medias:
        caption = i.dict()["caption_text"]
        try:
            file.write(f"{emoji.demojize(caption)} \n")
            print("I'm writing stuff")
        except Exception:
            try:
                file.write(f"{bytes(caption).decode('utf8', 'replace')} \n")
            except:
                file.write(f"{Exception} \n")
                print(Exception)
        
    file.close()
    file = open("text.txt", "r")
    print(file.read())

    print(medias[5])