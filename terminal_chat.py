import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")
django.setup()

from chatbot.chat import get_bot_response

print("Chatbot is running! Type 'exit' to quit.\n")

while True:
    user_input = input("user: ")

    if user_input.lower() == "exit":
        print("bot: Goodbye!")
        break

    response = get_bot_response(user_input)
    print("bot:", response)
