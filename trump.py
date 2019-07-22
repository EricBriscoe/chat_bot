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
                # if capital >= 1200:
                #     n = int(capital/1200)
                #     await message.channel.send(f"$$build steel mill {n}")
                #     capital -= 1200*n
                if capital >= 550:
                    n = int(capital / 550)
                    await message.channel.send(f"$$build iron mine {n}")
            elif "<@601238925813612575>, are you sure you want" in message.content:
                await message.add_reaction('\u2705')

        elif message.channel.id == 601256029501521930:
            if "maga" in message.content and message.author.id == 131835640827346944:
                while True:
                    await message.channel.send('$$sellall iron')
                    await message.channel.send("$$corp")
                    await asyncio.sleep(60)
            else:
                await message.channel.send(chatbot.get_response(message.content))

        chatbot.get_response(td.randomquote().quote)


if __name__ == "__main__":
    client = Player()
    client.run(os.environ["token"])
