from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "BotCorpus",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        "chatterbot.logic.BestMatch"
    ],
    database_uri='sqlite:///BotCorpus.db'
)
trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")
# trainer.train("chatterbot.corpus.bangla")
trainer.train("corpus.bangla")
trainer.train("corpus.english")
trainer.train("corpus.anglo_bangla")

def getResponse(message):
    response = chatbot.get_response(message)
    return response
