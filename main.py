mainLoop = True

def question(question):
    if question == "What is your name?":
        print("My name is James.")
    elif question == "What are you?":
        print("I am a chat bot.")
    elif question == "Are you cool?":
        print("Yes I am a very cool cat.")
    else:   
        print("I do not know that")


while mainLoop == True: 
    test = input("Enter Question: ")
    question(test)


