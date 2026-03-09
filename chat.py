from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot(
    'TerminalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)

# Train bot with English corpus
trainer.train("chatterbot.corpus.english")

def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return response
