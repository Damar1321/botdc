import discord
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} online!')
    # Biar ga mati
    while True:
        await asyncio.sleep(60)
        print("Bot masih hidup...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!ping':
        await message.channel.send('Pong!')

client.run(os.getenv('DISCORD_TOKEN'))
