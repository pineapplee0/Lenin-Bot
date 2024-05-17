import discord
import secrets

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # if any(x in ourstring for x in ["hello", "something else"])
    if any (word in message.content for word in ['my', 'mine', 'his', 'hers', 'theirs', 'has', 'have', 'own']):
        su_emoji = discord.utils.get(client.emojis, name='flag_su')
        await message.channel.send(f"{message.author.mention} Uh oh! It appears that you meant to say 'our'. In Soviet discord, there are no personal belongings.")
        await message.channel.send((str(su_emoji) + ' ') * 3)

client.run(secrets.token)
