import os
import time

import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Dr Buntu')
trainer = ChatterBotCorpusTrainer
trainer.train("chatterbot.corpus.english")


class Player(discord.Client):
    async def on_ready(self):
        print('Logged on as ', self.user)

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            time.sleep(.5)
            # await message.channel.send(chatbot.get_response(message.content))
            chatbot.get_response(message.content)
            return

        if message.channel.id == 601256029501521930:
            await message.channel.send(chatbot.get_response(message.content))
        else:
            chatbot.get_response(message.content)


if __name__ == "__main__":
    client = Player()
    client.run(os.environ['token'])
