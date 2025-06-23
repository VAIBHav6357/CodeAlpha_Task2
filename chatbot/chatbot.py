def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi there! 😊")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm doing great! Thanks for asking. How about you?")
        elif user_input in ["i'm good", "i'm fine", "doing well"]:
            print("🤖 Chatbot: Awesome! Glad to hear that. 🌟")
        elif user_input in ["i'm sad", "not good", "feeling low"]:
            print("🤖 Chatbot: I'm here for you. Want to talk about it? ❤️")
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I’m a simple chatbot created to talk with you!")
        elif user_input in ["what can you do", "help"]:
            print("🤖 Chatbot: I can chat with you and try to cheer you up! Ask me anything.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Take care. 👋")
            break
        else:
            print("🤖 Chatbot: Hmm, I didn't understand that. Can you rephrase? 🤔")

# Run the chatbot
chatbot()
