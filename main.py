import discord
import secrets

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_emoji(emoji_name):
    return str(discord.utils.get(client.emojis, name=emoji_name))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif any (word in message.content for word in ['my', 'mine', 'his', 'hers', 'theirs']):
        await message.channel.send(f"{message.author.mention} Uh oh! It appears that you meant to say 'our'. In Soviet discord, there are no personal belongings.")
        await message.channel.send((get_emoji('flag_su') + ' ') * 3)

    elif any (word in message.content for word in ['own', 'owns', 'has', 'have']):
        await message.channel.send(f"{message.author.mention} Comrade! When will you learn that you cannot have personal belongings in Soviet discord?")
        await message.channel.send(get_emoji('comrade'))

    elif any (word in message.content for word in ['our', 'comrade', 'lenin is the best!', 'soviet']):
        await message.channel.send(f"{message.author.mention} Yes, comrade! You are learning the valuable ways of Leninism, you will not be sent to the gulag! Cпасибо!")
        await message.channel.send("https://tenor.com/view/lenin-fun-pride-positivity-colorful-gif-18101101")

client.run(secrets.token)
