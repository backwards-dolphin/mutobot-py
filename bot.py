import discord
import os

TOKEN = os.environ['discord']
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        msg = 'Hello, {0.author.mention}'.format(message)
        await client.send_message(message.channel,msg)
    if message.content.startswith(".join"):
        user = message.author
        args = message.content.split(" ")
        args1 = ''.join(args[1:])
        if args1 == "hmag":
            role = discord.utils.get(user.server.roles, name ="hmag")
            try:
                await client.add_roles(user,role)
                await client.send_message(message.channel,"I've added you to hmag, {0.author.mention}".format(message))
            except:
                await client.send_message(message.channel,"I couldn't add you, {0.author.mention}".format(message))
        elif args1 == "cvel":
            role = discord.utils.get(user.server.roles, name ="cvel")
            try:
                await client.add_roles(user,role)
                await client.send_message(message.channel,"I've added you to cvel, {0.author.mention}".format(message))
            except:
                await client.send_message(message.channel,"I couldn't add you, {0.author.mention}".format(message))
        else:
            await client.send_message(message.channel,"Mmmm..what is that?")
    if message.content.startswith(".leave"):
        user = message.author
        args = message.content.split(" ")
        args1 = ''.join(args[1:])
        if args1 == "hmag":
            role = discord.utils.get(user.server.roles, name ="hmag")
            try:
                await client.remove_roles(user,role)
                await client.send_message(message.channel,"I've removed you from hmag, {0.author.mention}".format(message))
            except:
                await client.send_message(message.channel,"I couldn't remove you, {0.author.mention}".format(message))
        elif args1 == "cvel":
            role = discord.utils.get(user.server.roles, name ="cvel")
            try:
                await client.remove_roles(user,role)
                await client.send_message(message.channel,"I've removed you from cvel, {0.author.mention}".format(message))
            except:
                await client.send_message(message.channel,"I couldn't remove you, {0.author.mention}".format(message))
        else:
            await client.send_message(message.channel,"Mmmm..what is that?")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='Serving Tama'))
    print('------')

client.run(TOKEN)
