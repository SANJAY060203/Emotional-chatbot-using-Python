import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random

# Download necessary NLTK resources
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Predefined responses based on emotions
responses = {
    "positive": [
        "That's great to hear! 😊",
        "I'm so happy for you! 🎉",
        "Keep up the positive vibes! 🌟"
    ],
    "negative": [
        "I'm sorry to hear that. 😢",
        "Is there anything I can do to help? 🤗",
        "Stay strong; things will get better. 💪"
    ],
    "neutral": [
        "I see. Could you tell me more?",
        "Hmm, that's interesting.",
        "Alright, let me know if there's more to it."
    ]
}

def analyze_emotion(text):
    """Analyze the sentiment of the input text."""
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] > 0.05:
        return "positive"
    elif sentiment_score['compound'] < -0.05:
        return "negative"
    else:
        return "neutral"

def chatbot():
    """Run the emotional chatbot."""
    print("Emotional Chatbot: Hi there! How are you feeling today?")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Emotional Chatbot: Take care! Goodbye! 👋")
            break
        
        # Analyze user input and get emotion
        emotion = analyze_emotion(user_input)
        
        # Choose a random response based on the emotion
        bot_response = random.choice(responses[emotion])
        print(f"Emotional Chatbot: {bot_response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
