import random

# Basic chatbot response logic
def generate_response(user_input):
    responses = {
        "hi": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
        "how are you": ["I'm doing great! How about you?", "I'm fine, thanks for asking!"],
        "bye": ["Goodbye!", "See you soon!", "Take care!"],
    }
    
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."
