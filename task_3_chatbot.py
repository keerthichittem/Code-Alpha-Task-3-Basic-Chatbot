def chatbot():

    print("====================================")
    print("      MY SIMPLE CHATBOT")
    print("====================================")
    print("Type 'exit' to end the conversation.\n")

    while True:

        user = input("You : ").strip().lower()

        if user == "hello":
            print("Bot : Hello! Welcome to my chatbot.")

        elif user == "hi":
            print("Bot : Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot : I'm doing well. Thanks for asking!")

        elif user == "what is your name":
            print("Bot : My name is SmartBot.")

        elif user == "who created you":
            print("Bot : I was developed using Python.")

        elif user == "what can you do":
            print("Bot : I can answer a few basic questions.")

        elif user == "thank you":
            print("Bot : You're welcome!")

        elif user == "bye" or user == "exit":
            print("Bot : Goodbye! Have a great day.")
            break

        else:
            print("Bot : Sorry, I don't understand that question.")

chatbot()
