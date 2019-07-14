
import discord
import requests
import random


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itselfy
        if message.author.id == self.user.id:
            return
        else:
            com = message.content
            mid = message.author.id
            print(mid)
            print(com)
            if mid == 486529234123096064:
                await message.add_reaction(':CC:599634991756083223')
            if com.startswith('!hello'):
                await message.channel.send('Hello {0.author.mention}'.format(message))


client = MyClient()
token = read_token()
client.run(token)
