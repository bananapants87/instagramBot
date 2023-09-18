import time, keyring, emoji, login, like, dm, userID

def runBot():
    print("Bot is running, you just have to wait lol.")
    cl = login.cl

    loginPromptString = "Press any key to insert the username of the account you wish to interact with or 'q' to exit the program: "
    userinput = str(input(loginPromptString))

    while userinput.lower() != 'q':

        username = userID.InsertUsername(input("Enter the username: "))
        
        secondPromptString = "Press 1 to access DM functions\n2 to access LIKE functions\n3 to access POSTINFO functions\nor 'q' to exit the program"
        
        userinput2 = str(input(secondPromptString))
        
        while userinput2.lower() != 'q':
            
            if userinput2 == '1':
                DMPrompt = "Press 1 to spam DM the selected user."
                DMInput = str(input(DMPrompt))
                if DMInput == '1':
                    dm.spamMessageSingle(userID.findUserID(username))
                    
            userinput2 = str(input(secondPromptString))
        
        userinput = str(input(loginPromptString))

        #print(user_id2Info)
        #print(medias2)

        
