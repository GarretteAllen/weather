import discord
import requests
import json
from weather import error, parse_data, weather_messages

token = 'DISCORDBOTTOKEN'
rak = 'RAPIDAPIKEY'
intents = discord.Intents.default()
intents.message_content = True
command_prefix = '!weather'
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix} [location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix, '').lower()
        if len(location) >= 1:
            url = f'https://yahoo-weather5.p.rapidapi.com/weather?rapidapi-key={rak}&location={location}'
            #try:
            data = json.loads(requests.get(url).content)
            data = parse_data(data)
            await message.channel.send(embed=weather_messages(data, location))
            #except KeyError:
                #await message.channel.send(embed=error(location))

client.run(token)