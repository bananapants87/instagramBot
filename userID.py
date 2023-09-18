import login

GlobalUsername = ""
mediaNumber = 20
user_id = ''
medias = None
cl = login.cl

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

def getMedias(userID):
    global medias
    medias = cl.user_medias(user_id, mediaNumber)
    return medias


#user_idInfo = cl.user_info_by_username(GlobalUsername).dict()
#medias = cl.user_medias(user_id, mediaNumber)
