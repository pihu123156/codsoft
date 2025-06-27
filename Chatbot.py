def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected!")

        elif "your name" in user_input:
            print("Chatbot: I'm called SimpleBot.")

        elif "help" in user_input:
            print("Chatbot: Sure, I can help. You can ask me about the weather, my name, or how I'm doing.")

        elif "weather" in user_input:
            print("Chatbot: I can't check the weather now, but it's always a good idea to look outside or use a weather app!")

        else:
            print("Chatbot: Sorry, I don't understand that. Try asking something else.")

# Run the chatbot
chatbot()
