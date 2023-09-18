import login, time

cl = login.cl

def spamMessageSingle(userID):
    inputList = []
    while True:
        userinput = str(input("Enter a single line or enter 'stop' to stop typing: "))
        if userinput.lower() == 'stop':
            break
        else:
            inputList.append(userinput)
    
    for i in inputList:
        cl.direct_send(text=i, user_ids=[userID])
        time.sleep(2)      
    return