import pandas as pd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from tqdm import tqdm

chatbot = ChatBot('Dr Buntu')


def train_tech():
    trainer = ChatterBotCorpusTrainer
    trainer.train("chatterbot.corpus.english")
    data = pd.read_csv('data/testset.csv')

    previous_message = ''
    for index, row in tqdm(data.iterrows()):
        if row[0] == previous_message:
            continue
        previous_message = row[0]
        if '__EOS__' in previous_message:
            chatbot.get_response(previous_message.split('__EOS__')[0])
            chatbot.get_response(previous_message.split('__EOS__')[1])


def train_movies():
    trainer = ChatterBotCorpusTrainer
    trainer.train("chatterbot.corpus.english")
    with open('data/movie_lines.txt', 'r') as file:
        data = file.read()
    data = data.split('\n')
    for line in tqdm(data):
        chatbot.get_response(line.split('+++$+++')[-1])


def list_train_movies():
    trainer = ListTrainer(chatbot)
    with open('data/movie_lines.txt', 'r') as file:
        data = file.read()
    data = data.split('\n')
    trainer.train(conversation=[line.split('+++$+++')[-1] for line in data])


if __name__ == "__main__":
    list_train_movies()
