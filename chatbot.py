
def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hi!")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
