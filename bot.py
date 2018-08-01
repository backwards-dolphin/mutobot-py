import discord
from discord.ext import commands
import os
import re
from datetime import datetime, time
import asyncio

TOKEN = os.environ['discord']
command_prefix = '.'
client = commands.Bot(command_prefix=command_prefix)
owner = ["89973782285910016"]
supportedRoles = ["notifications","hmag","cvel","lomien"]
extensions = ['starsim', 'training', 'strings', 'poll', 'bossqueue']

client.remove_command('help')

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='in Tama | .help'))

@client.event
async def on_member_join(member):
    tama = "404103946328866818"
    if member.server.id == tama:
        welcome = client.get_channel("408318436192550924") # 408318436192550924
        rules = client.get_channel("404439224973000704")
        await client.send_message(welcome, "Welcome to Tama, " + member.mention + "! Please read the " + rules.mention + " to register! Be sure to introduce yourself to everyone!")
    # add logic here --> user posts username and send message to JRS channel for confirmation s

async def reset_notifications():
    notifications = discord.Object(id="468950573497057332")
    await client.wait_until_ready()
    flagraces = [12,19,21,22,23]
    while True:
        if datetime.utcnow().hour in flagraces and datetime.utcnow().minute == 0:
            msg = await client.send_message(notifications,"Guild flag race commencing! Be sure to help out Tama!")
            await asyncio.sleep(1800)
            await client.delete_message(msg)
        if datetime.utcnow().hour == 0 and datetime.utcnow().minute == 0:
            if (datetime.today().weekday() == 6):
                msg = await client.send_message(notifications,"Reset time! Meet up with your guild members in CH18 Root Abyss. Be sure to collect your guild potions too!")
            elif (datetime.today().weekday() == 3):
                msg = await client.send_message(notifications,"Weekly reset time! Meet up with your guildies in CH18 Root Abyss.")
            else:
                msg = await client.send_message(notifications,"Reset time! Meet up with your guildies in CH18 Root Abyss.")
            await asyncio.sleep(1800)
            await client.delete_message(msg)
        await asyncio.sleep(60 - datetime.utcnow().second)


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
async def register(ctx, msg):
    tama = client.get_server("404103946328866818")
    smolEgg = discord.utils.get(ctx.message.server.roles, name="Smol Egg")
    newEgg = discord.utils.get(ctx.message.server.roles, name="egg")
    if ctx.message.server == tama:
        if smolEgg in ctx.message.author.roles:
            await client.say("You are already a member!")
        else:
            jrChannel = client.get_channel("405565182891261963")
            await client.change_nickname(ctx.message.author, ctx.message.author.name + " (" + msg + ")")
            await client.say("The JRs have been notified! We will verify you soon.")
            msg = await client.say("We also have a beginner role for new players! Would you like to join?")
            await client.add_reaction(msg,'👍')
            await client.add_reaction(msg,'👎')
            res = await client.wait_for_reaction('👍', message=msg, timeout=600)
            if res.user is not None:
                if res.user is ctx.message.author:
                    await client.add_roles(ctx.message.author, newEgg)
                    await client.say("I've added you to the role. Enjoy your stay!")
            await client.send_message(jrChannel, ctx.message.author.mention + " has joined and verified their username. Please user .member {@mention} to verify.")
    else:
        await client.say("You are not in Tama!")

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

@client.command(pass_context=True)
async def join(ctx, role):
    user = ctx.message.author
    if role in supportedRoles:
        assign = discord.utils.get(user.server.roles, name=role)
        await client.add_roles(user,assign)
        await client.say("I've added you to " + role + ", " + ctx.message.author.mention)
    else:
        await client.say("Invalid role! Please check ``.help`` for supported roles")

@client.command(pass_context=True)
async def leave(ctx, role):
    user = ctx.message.author
    if role in supportedRoles:
        assign = discord.utils.get(user.server.roles, name=role)
        await client.remove_roles(user,assign)
        await client.say("I've removed you from " + role + ", " + ctx.message.author.mention)
    else:
        await client.say("Invalid role! Please check ``.help`` for supported roles")

@client.command(pass_context = True)
@commands.has_permissions(manage_roles = True)
async def member(ctx):
     memberAdd = discord.utils.get(ctx.message.server.roles, name="Smol Egg")
     verifiedAdd = discord.utils.get(ctx.message.server.roles,name="Verified")
     await client.add_roles(ctx.message.mentions[0], memberAdd, verifiedAdd)
     await client.say("Added!")

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("cogs." + extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))

client.loop.create_task(reset_notifications())
client.run(TOKEN)
