import discord
from discord.ext import commands
import os
import re
from strings import *
from datetime import datetime, time
import asyncio

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
    await client.change_presence(game=discord.Game(name='in Tama | .help'))

@client.event
async def on_member_join(member):
    welcome = client.get_channel("408318436192550924") # 408318436192550924
    await client.send_message(welcome, "Welcome to Tama, " + member.mention + "! Please real the #rules to register! Be sure to introduce yourself to everyone!")
    # add logic here --> user posts username and send message to JRS channel for confirmation s

async def reset_notifications():
    notifications = discord.Object(id="467921304478023681")
    await client.wait_until_ready()
    while not client.is_closed:
        timeNow = datetime.now().time()  # Fetch current time
        timeFormat = timeNow.replace(second=0,microsecond=0)  # Format to 00:00000
        timeReset = datetime.now().time().replace(hour=20,minute=0,second=0,microsecond=0)

        if timeFormat.hour in {8, 15, 17, 18, 19} and timeFormat.minute == 0:
            await client.send_message(notifications,"Guild flag race commencing! Be sure to help out Tama!")
            if timeFormat.hour == 8:
                print("Sleeping for 6 hours and 50 minutes til next flag race")
                print("Formatted time 1st Flag: " + str(timeFormat))
                await asyncio.sleep(25200)
                return
            else:
                print("Sleeping for around an hour til next flag race")
                print("Formatted time Other Flags: " + str(timeFormat))
                await asyncio.sleep(3600)
                return

        if timeFormat == timeReset:
            if (datetime.today().weekday() == 6):
                await client.send_message(notifications,"Reset time! Meet up with your guildies in CH18 Root Abyss. Be sure to collect your guild potions too!")
            else:
                await client.send_message(notifications,"Reset time! Meet up with your guildies in CH18 Root Abyss.")
            print("Sleeping for 12 hours for the next reset")
            print("Formatted time: " + str(timeFormat))
            time.sleep(43200)
            return # Return to next reset

        print("Sleeping for 60 seconds..")
        await asyncio.sleep(60)

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
        print("Some error has been thrown!")

@client.event
async def on_message(message):
    if message.content.startswith(".."):
        return
    await client.process_commands(message)

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
async def register(ctx, msg):
    tama = client.get_server("404103946328866818")
    smolEgg = discord.utils.get(ctx.message.server.roles, name="Smol Egg")
    if ctx.message.server == tama:
        if smolEgg in ctx.message.author.roles:
            await client.say("You are already a member!")
        else:
            jrChannel = client.get_channel("405565182891261963")
            await client.change_nickname(ctx.message.author, ctx.message.author.name + " (" + msg + ")")
            await client.say("The JRs have been notified! We will verify you soon.")
            await client.send_message(jrChannel, ctx.message.author.mention + " has joined and verified their username. Please user .member {@mention} to verify.")
    else:
        await client.say("You are not in Tama!")

@client.command(pass_context = True)
async def train(ctx, level, range = 7):
    try:
        iLvl = int(level)
        iRange = int(range)
    except:
        await client.say("Please enter numbers, not letters!")
        return
    # call dictionary for levels from strings.py and output results in discord format - embed maybe
    if iRange <= 20:
        levelDict = getTrainDict()
        string = ""
        embed=discord.Embed(title="Training spots", color=0xffdd88)
        embed.set_thumbnail(url="https://i.imgur.com/LpZoKi7.png")
        for key, value in levelDict.items():
            if iLvl - iRange < key < iLvl + iRange:
                embed.add_field(name="Level " + str(key), value=value, inline=False)
        embed.set_footer(text="If you have training spot suggestions or find an error please contact @colin#0001")
        await client.say(embed=embed)
    else:
        await client.say("Please use a smaller range! (less than 20)")

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

@commands.has_permissions(manage_roles = True)
@client.command(pass_context=True)  # Taken from github/Vexs but formatted
async def quickpoll(ctx, *, options: str):

    list1 = options.split("|")
    question = list1[0] # Get the question
    entries = list1[1:] # Get the answers

    if len(entries) <= 1:
        await client.say('You need more than one option to make a poll!')
        return
    if len(entries) > 11:
        await client.say('You cannot make a poll for more than 10 things!')
        return

    if len(entries) == 2 and entries[0] == 'yes' and entries[1] == 'no':
        reactions = ['✅', '❌']
    else:
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    description = ""
    for x, option in enumerate(entries):
        description += '\n{} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=description, color=0xffdd88)
    embed.set_thumbnail(url="https://i.imgur.com/LpZoKi7.png")
    react_message = await client.say(embed=embed)
    for reaction in reactions[:len(entries)]:
        await client.add_reaction(react_message, reaction)
    embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    await client.edit_message(react_message, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(manage_roles = True)
async def member(ctx):
     memberAdd = discord.utils.get(ctx.message.server.roles, name="Smol Egg")
     await client.add_roles(ctx.message.mentions[0], memberAdd)
     await client.say("Added!")

client.loop.create_task(reset_notifications())
client.run(TOKEN)
