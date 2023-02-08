import discord
import os
import json
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("KEY")
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='ben', intents=intents)

with open('custom.json', 'r',encoding='utf-8') as f:
    commands = json.load(f)

with open('expressions.json','r',encoding='utf-8') as f:
    expressions = json.load(f)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="Grand Ben Auto 5", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower().startswith("ben"):

        content = message.content[3:].strip()

        # if content == "" or content == "?":
        #     return await message.channel.send('https://tenor.com/view/ben-yes-yes-fthememer-phone-call-yes-call-yes-gif-24938145')

        # for command in commands:
        #     if command in content:
        #         return await message.channel.send(commands[command])
        
        # # if "rap" in content:
        # #     voicechannel = discord.utils.get(message.guild.channels, name='Musique Baron')
        # #     vc = await voicechannel.connect()
        # #     vc.play(discord.FFmpegPCMAudio("talking_ben.mp3"executable="./bin/ffmpeg.exe"))
        # #     return

        # prompt = f"Répond uniquement par 'Yess','No','Arghhhh' ou 'Ohohoh' à ça : {content}"
        # response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=300)
        # response = response["choices"][0]["text"]

        # for expression in expressions:
        #     if expression in response:
        #         return await message.channel.send(expressions[expression])



        response = openai.Completion.create(model="text-davinci-003", prompt=content, temperature=0, max_tokens=300)
        response = response["choices"][0]["text"]
        await message.channel.send(response)
        
client.run(os.getenv("TOKEN"))