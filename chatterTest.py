from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#define parameters for chatterbot
chatterbot = ChatBot("Test Bot")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train(
    #train on the included english language corpus
    "chatterbot.corpus.english",
)
print("This is a simple test of the Chatterbot API\nGo ahead and ask it something\nWhen you are done just type exit")
test = True
while test:
    #collect user input
    print ("-> ")
    text = input();
    #terminate on user command
    if text == "exit":
        test = False
    else:
        #generate a generic response
        response = chatterbot.get_response(text)
        print(response)