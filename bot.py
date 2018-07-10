import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import re
from strings import *

TOKEN = os.environ['discord']
command_prefix = '.'
client = commands.Bot(command_prefix=command_prefix)
owner = ["89973782285910016"]
adminRoles = ["Eggcellent", "Tama-sama", "memer"]

client.remove_command('help')

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_member_join(member):
    welcome = client.get_channel("408318436192550924")
    pass
    # add logic here --> user posts username and send message to JRS channel for confirmation

@client.event
async def on_command_error(error, ctx):
    # await client.send_message(ctx.message.channel, "Invalid arguments!")
    pass
@client.command(pass_context = True, hidden = True)
async def logout(ctx):
    if ctx.message.author.id in owner:
        try:
            await client.say("Logging out bot")
            await client.close()
        except:
            await client.say("Failed to log out bot")
    else:
        await client.say("You do not have permissions to do this")
        return

@client.command(pass_context = True)
async def help(ctx):
    await client.say("I've sent you a PM, " + ctx.message.author.mention)
    await client.send_message(ctx.message.author, getHelp())

@client.command()
async def cap():
    await client.say(getCap())

@client.command(pass_context = True)
async def stamp(ctx, *, msg):
    string = ""
    for letter in (re.sub('[^a-zA-Z!?]+', '', msg)):
        if letter is 'b' or letter is 'B':
            string+=":b:"
        elif letter is '?':
            string+=":question:"
        elif letter.isalpha():
            string+=":regional_indicator_" + letter.lower() + ": "
        else:
            pass
    if string == "":
        await client.say("Invalid Input!")
    await client.say(string)


client.run(TOKEN)
