# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# creating a chatbot
myBot = ChatBot(
    name='prophet',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ]
)

# training the chatbot
small_convo = [
    'hello bot',
    'Hi user',
    'How are you doing?',
    'How are you?',
    "I'm all good, thanks for asking.",
    'Always cool.',
    'I\'m Okay',
    'Glad to hear that.',
    'I\'m fine',
    'I feel awesome',
    'Excellent, glad to hear that.',
    'Not so good',
    'Sorry to hear about that.',
    'What\'s your name?',
    "I\'m prophet. you can Ask me a compute science question, i'll be glad to answer."
]

convo_1 = [
    'who designed C language',
    'Dennis Ritchie'
]

convo_2 = [
    'When was C language designed',
    'It was designed in the year 1969-1973'
]

convo_3 = [
    'List some features of python',
    "Free and Open-Source, Robust Standard Library, Interpreted, Portable, Object-Oriented, Extensible."
]

convo_4 = [
    'Where can we use python',
    "It can be applied to feilds such as data science, cloud computing, big data, AI etc"
]

convo_5 = [
    'can you help me with a contact method',
    "contact us through E-mail - abc@xyz.com, phone number - 1234567891",
]

x=[small_convo,convo_1,convo_2,convo_3,convo_4,convo_5]

# using the ListTrainer class
list_trainee = ListTrainer(myBot)
for i in (x):
    list_trainee.train(i)

# using the ChatterBotCorpusTrainer class
corpus_trainee = ChatterBotCorpusTrainer(myBot)
corpus_trainee.train('chatterbot.corpus.english')

j=1
while(j!=0):
    a=input(">>> ")
    print(myBot.get_response(a))
    #ch=input("enter choice y/n")
    #if ch=='n' or ch=='N':
    j=j+1