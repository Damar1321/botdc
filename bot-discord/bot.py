import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot {client.user} sudah online!')
    print(f'📍 Masuk ke Discord sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!ping':
        await message.channel.send('Pong! 🏓')
    
    if message.content == '!halo':
        await message.channel.send(f'Halo {message.author.mention}! 👋')

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("❌ ERROR: Token tidak ditemukan!")
    print("📝 Buat file .env dengan isi: DISCORD_TOKEN=token_anda_disini")
    exit(1)

client.run(TOKEN)
