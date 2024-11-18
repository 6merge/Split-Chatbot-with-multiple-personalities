import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the Generative AI model with the API key
genai.configure()
model_name = "gemini-1.5-flash"

# Define themes/tones with subtle behavioral prompts
styles = {
    "casual": "Keep responses natural and conversational.",
    "formal": "Keep responses clear and professional.",
    "friendly": "Keep responses warm and supportive.",
    "witty": "Include subtle humor where appropriate.",
    "direct": "Keep responses brief and to the point."
}

def select_style():
    print("\nAvailable styles:")
    for key in styles.keys():
        print(f"- {key}")
    chosen_style = input("\nChoose a style: ").lower().strip()
    if chosen_style in styles:
        print(f"Style set to: {chosen_style}\n")
        return styles[chosen_style]
    print("Invalid style selected. Using casual style.\n")
    return styles["casual"]

# Initial setup
current_style = select_style()
print("Chatbot ready! Type 'quit' to end or 'style' to change style.\n")

# Chat loop
while True:
    prompt = input("You: ")
    
    if prompt.lower().strip() == "quit":
        print("Goodbye!")
        break
        
    if prompt.lower().strip() == "style":
        current_style = select_style()
        continue
    
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            f"System: {current_style}\nUser: {prompt}\nAssistant: Respond directly without mentioning your tone or style."
        )
        
        if response:
            print(f"Bot: {response.text}")
        else:
            print("Bot: (No response received)")
            
    except Exception as e:
        print(f"Bot: Error: {e}")