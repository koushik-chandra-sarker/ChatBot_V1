from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "Bot_Waysis",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': '%Bot_Waysis_False%',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatbot)


def trainModel(dataset):
    conversation = []
    for data in dataset:
        conversation.append(data.question)
        conversation.append(data.answer)
    # chatbot.storage.drop()
    trainer.train(conversation)


def getResponse(message):
    response = chatbot.get_response(message)

    return response
