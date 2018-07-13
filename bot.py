import discord
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
    await client.change_presence(game=discord.Game(name='Feeding on Tama | .help'))

@client.event
async def on_member_join(member):
    welcome = client.get_channel("408318436192550924") # 408318436192550924
    await client.send_message(welcome, "Welcome to Tama, " + member.mention + "! Please real the #rules to register! Be sure to introduce yourself to everyone!")
    # add logic here --> user posts username and send message to JRS channel for confirmation s

@client.event
async def on_command_error(error,ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await client.send_message(ctx.message.channel,"This command cannot be used in private messages.")

    elif isinstance(error, commands.DisabledCommand):
        await client.send_message(ctx.message.channel,"This command is disabled and cannot be used.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await client.send_message(ctx.message.channel,"You are missing required arguments!")

    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await client.send_message(ctx.message.channel,"Unknown error!")

@client.event
async def on_message(message):
    if message.content.startswith(".."):
        return
    await client.process_commands(message)

@client.command(pass_context = True, hidden = True)
async def logout2(ctx):
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
async def register(ctx, msg):
    jrChannel = client.get_channel("405565182891261963")
    await client.change_nickname(ctx.message.author, ctx.message.author.name + " (" + msg + ")")
    await client.say("The JRs have been notified! We will verify you soon.")
    await client.send_message(jrChannel, ctx.message.author.mention + " has joined and verified their username. Please user .member {@mention} to verify.")

@client.command(pass_context = True)
async def train(ctx, level, range = 7):
    try:
        iLvl = int(level)
        iRange = int(range)
    except:
        await client.say("Please enter numbers, not letters!")
        return
    # call dictionary for levels from strings.py and output results in discord format - embed maybe
    levelDict = getTrainDict()
    string = ""
    embed=discord.Embed(title="Training spots", color=0xffdd88)
    embed.set_thumbnail(url="https://i.imgur.com/LpZoKi7.png")
    for key, value in levelDict.items():
        if iLvl - iRange < key < iLvl + iRange:
            embed.add_field(name="Level " + str(key), value=value, inline=False)
    embed.set_footer(text="If you have training spot suggestions or find an error please contact @colin#0001")
    await client.say(embed=embed)

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


@client.command(pass_context = True)
@commands.has_permissions(manage_roles = True)
async def member(ctx):
     memberAdd = discord.utils.get(ctx.message.server.roles, name="Smol Egg")
     await client.add_roles(ctx.message.mentions[0], memberAdd)
     await client.say("Added!")

client.run(TOKEN)
