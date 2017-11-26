from chatterbot import ChatBot

bot = ChatBot(
    'Abd_bot',
    #trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.sqlite3'
)


while True:
    try:
     #bot.train("chatterbot.corpus.english")
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

# # Train based on the english corpus
# chatbot.train("chatterbot.corpus.english")

# # Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")