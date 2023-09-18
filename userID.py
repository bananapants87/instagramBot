import login

GlobalUsername = ""
mediaNumber = 20
user_id = ''

def InsertUsername(userinput):
    global GlobalUsername
    GlobalUsername = userinput
    return GlobalUsername

def numberOfMedias(number=20):
    global mediaNumber
    mediaNumber = number
    
def findUserID(username):
    global user_id 
    user_id = cl.user_id_from_username(GlobalUsername)
    return user_id

print(f"{GlobalUsername}, {mediaNumber}")

cl = login.cl



#user_idInfo = cl.user_info_by_username(GlobalUsername).dict()
#medias = cl.user_medias(user_id, mediaNumber)
