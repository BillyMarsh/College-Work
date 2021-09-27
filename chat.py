name = input("What is your name?: ")

mainLoop = True

def question(question):
    if question == "What is your name?":
        print("My name is James, I know yours is", name, ".")
    elif question == "What are you?":
        print("I am a chat bot.")
    elif question == "Are you cool?":
        print("Yes I am a very cool cat.")
    elif question == "exit":
        exit()
    else:   
        print("I do not know that")


while mainLoop == True: 
    test = input("Enter Question: ")
    question(test)
