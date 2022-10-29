import discord

color = 0xFF6500
key_features = {
    'temperature' : 'Temperature',
    'text' : 'Condition'
}

def parse_data(data):
    data = data['current_observation']['condition']
    del data['code']
    return data

def weather_messages(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'The current weather for {location}.',
        color=color)
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key])
        )
    return message

def error(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving data for {location}',
        color=color
    )