import discord
from discord.ext import commands
import time

class strings:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
        msg = """```md
[ MutoBot version 1.0 ]
-----------------------
[ = A Tama Helper = ]
=====================
< Admin Commands >
.member (mention)
#Adds member to Smol Egg role

< Commands >
.help
#Displays commands accepted by Muto
.cap
#Displays capping information
.join (role)
#Allows you to join a role for carries
.leave (role)
#Allows you to leave a role if you've gotten your carries
.stamp (text)
#Converts your text to big letters
.register (username)
#Registers you so a Jr can approve your membership
.train (level) {range?}
#Searches for good training spots around your level
#{range} is optional if you wish to broaden your search
.star (money) {star level?}
#Simulates your odds on getting 22* or specified stars based on money
#Example: .star 5.2b 15

< Supported roles >
#hmag
#cvel
#notifications```"""
        await self.client.say("I've sent you a PM, " + ctx.message.author.mention)
        await self.client.send_message(ctx.message.author, msg)

    @commands.command(pass_context=True)
    async def cap(self, ctx):
        msg = """```md
[ Capping ]
------------
Capping is essential for Tama to grow into a real guild.
You can cap simply by going to Ch 18 during reset time and finding
a party that is capping, or ask others yourself in guild chat.
Root Abyss is the most common way to start capping. Most people run:
Crimson Queen --> Pierre --> VonBon --> Vellum --> NMagnus/CHT
---------------------------------------------------------------
This can help our guild grow, as well as help you get your 10 RA runs!```"""
        await self.client.say(msg)

time.sleep(1)
def setup(client):
    client.add_cog(strings(client))
