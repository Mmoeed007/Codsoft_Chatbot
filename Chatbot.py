def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created to assist you.",
        "who are you": "I am a chatbot designed to help with your queries.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! If you have any other questions, feel free to ask."
    }

    for pattern, response in responses.items():
        if pattern in user_input:
            return response
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user_input))