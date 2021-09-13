def botText(bot):
    print("")
    print("James #~", bot)
    print("")

def userText(user, text):
    print("")
    print(user, "#~", text)
    print("")

name = input("What is your name? ")
bool = False


while bool == False:
    if name is not None:
        bool = True
        main()



def mainUser(question):
    main = 10
    

def mainBot(question):
    if question == "What is your name?":
        botText("Hey there, my name is James!")
    elif question == "How are you today?":
        botText("I am pretty snazzy bro.")


    
