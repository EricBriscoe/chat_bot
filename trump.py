import asyncio
import os
import re
import time

import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tronalddump import TronaldDump

chatbot = ChatBot("Dr Buntu")
trainer = ChatterBotCorpusTrainer
trainer.train("chatterbot.corpus.english")

td = TronaldDump()


class Player(discord.Client):
    async def on_ready(self):
        print("Logged on as ", self.user)

    async def on_message(self, message):
        time.sleep(1)
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.author.id == 601241235474350122:
            if "Waifu God's Corporation" in message.content:
                capital = float(re.findall(
                    ":dollar: Capital: \*\*\$([0-9,\.]+)\*\*", message.content
                )[0].replace(',', ''))
                if capital >= 550 + 73:
                    n = int(capital / (550 + 73))
                    await message.channel.send(f"$$buy land {n}")
                    await asyncio.sleep(4)
                    await message.channel.send(f"$$build iron mine {n}")
            elif "<@601238925813612575>, are you sure you want" in message.content:
                await message.add_reaction('\u2705')

        if message.channel.id == 601256029501521930:
            print(message)
            print(message.type)
            print(message.embeds)
            if "maga" in message.content and message.author.id == 131835640827346944:
                while True:
                    await message.channel.send('$$sellall iron')
                    await asyncio.sleep(30)
                    await message.channel.send("$$corp")
                    await asyncio.sleep(30)
            else:
                await message.channel.send(chatbot.get_response(message.content))
        else:
            chatbot.get_response(td.randomquote().quote + message.content)

        chatbot.get_response(td.randomquote().quote)


if __name__ == "__main__":
    client = Player()
    client.run(os.environ["token"])
