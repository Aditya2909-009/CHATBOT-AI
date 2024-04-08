import random
import datetime
import os
import webbrowser

def get_response(user_input):
    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm doing well, thank you!",
        "bye": "Goodbye!",
        "goodbye": "See you later!",
        "what is your name": "I'm JARVIS!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "who are you": "I'm JARVIS a chatbot created to assist you.",
        "how old are you": "I don't have an age, I'm just a program!",
        "what can you do": "I can chat with you, tell jokes, and provide information.",
        "where are you from": "I exist in the digital world, here to help you!",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!",
        "open google": "Opening Google...",
        "open youtube": "Opening YouTube...",
        "default": "I'm not sure I understand. Can you try asking something else?"
    }

    # Convert user input to lowercase for case insensitivity
    user_input = user_input.lower()

    # Check if the user input matches any predefined responses
    if user_input in responses:
        if user_input == 'open google':
            webbrowser.open("https://www.google.com")
        elif user_input == 'open youtube':
            webbrowser.open("https://www.youtube.com")
        return responses[user_input]
    else:
        return responses["default"]

def main():
    print("Welcome to the JARVIS assistant!")
    print("You can start chatting. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_response(user_input)
        print("JARVIS:", response)

if __name__ == "__main__":
    main()

