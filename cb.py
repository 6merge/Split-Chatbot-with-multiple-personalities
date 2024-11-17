import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the Generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define themes
themes = {
    "default": "",
    "friendly": "Respond in a cheerful and friendly tone.",
    "professional": "Respond in a formal and concise tone.",
    "quirky": "Respond with humor and playful language.",
}

# Define tones
tones = {
    "casual": "Use a relaxed and informal communication style.",
    "formal": "Maintain a professional and structured communication style.",
    "empathetic": "Show understanding and emotional awareness in responses.",
    "educational": "Explain concepts clearly as if teaching.",
    "motivational": "Provide encouraging and inspiring responses."
}

# Function to select theme
def select_theme():
    print("\nAvailable themes:")
    for key in themes.keys():
        print(f"- {key}")
    chosen_theme = input("\nChoose a theme: ").lower().strip()
    if chosen_theme in themes:
        print(f"Theme set to: {chosen_theme.capitalize()}\n")
        return themes[chosen_theme]
    else:
        print("Invalid theme selected. Using default theme.\n")
        return themes["default"]

# Function to select tone
def select_tone():
    print("\nAvailable tones:")
    for key, description in tones.items():
        print(f"- {key}: {description}")
    chosen_tone = input("\nChoose a tone: ").lower().strip()
    if chosen_tone in tones:
        print(f"Tone set to: {chosen_tone.capitalize()}\n")
        return tones[chosen_tone]
    else:
        print("Invalid tone selected. Using casual tone.\n")
        return tones["casual"]

# Initial setup
print("Welcome to the Chatbot! Let's customize your experience.")
current_theme = select_theme()
current_tone = select_tone()

print("\nChatbot is ready! Type 'quit chat' to end the conversation, 'change theme' to select a new theme, or 'change tone' to select a new tone.\n")

# Chat loop
while True:
    # Take user input
    prompt = input("You: ")
    
    # Check for the exit command
    if prompt.lower().strip() == "/q":
        print("Chatbot: Goodbye! Have a great day!")
        break
        
    # Check for theme change
    if prompt.lower().strip() == "change theme":
        current_theme = select_theme()
        continue
        
    # Check for tone change
    if prompt.lower().strip() == "change tone":
        current_tone = select_tone()
        continue
    
    # Provide immediate feedback
    print("Chatbot: Generating response...")

    try:
        # Combine theme and tone as system context
        system_context = f"{current_theme} {current_tone}".strip()
        if system_context:
            system_context += " "

        # Create the full prompt
        full_prompt = f"{system_context}{prompt}"
        
        # Generate a response using the chat method
        response = genai.chat(
            model="chat-bison-001",  # Use an available chat model
            messages=[{"content": full_prompt, "author": "user"}],
        )

        # Extract and print the response content
        if response and "candidates" in response:
            print(f"Chatbot: {response.candidates[0]['content']}")
        else:
            print("Chatbot: (No meaningful response received.)")

    except Exception as e:
        print(f"Chatbot: An error occurred: {e}")
