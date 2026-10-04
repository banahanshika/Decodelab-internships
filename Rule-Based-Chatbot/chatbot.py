print("=====================================")
print("      welcome to the AI chatbot")
print("=====================================")
print("to end chat type 'bye', 'quit', 'exit'")

while True:
    user_input= input("you:  ").lower().strip()
    #for exit the chat
    if user_input in["bye","exit","quit"]:
          print("Bot : goodbye! have a great day")
          break
    #greetings
    elif user_input in["hii","hello","hey","hi"]:
         print("Bot: hello! how can i help you?")

    #introduction
    elif user_input in["who are you","what are you"]:
         print("Bot : i am simple rule-based AI chatbot") 

    #name
    elif user_input in ["what is your name"]:
         print("bot: my name is minibot")

    #how are you
    elif user_input in ["how are you", "how are you?"]:
         print ("Bot : i am doing great! Thanks for asking")

    # thnk you
    elif user_input in["thnks", "thnk you"]:
         print("Bot : you're welcome!")

    #about your day
    elif user_input in ["how was your day"]:
         print("Bot: It was great today. thank you for asking!")
    #help
    elif user_input in ["help", "what can you do"]:
         print("Bot: I can respond to greetings, answer simple questions and say goodbye")

    #unkown input
    else:
         print (" Bot : sorry , i dont understand ask something else")