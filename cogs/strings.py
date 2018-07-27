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

    @commands.command(pass_context=True)
    async def post200(self, ctx):
        msg = """```md
[ Post Level 200 ]
------------------
After level 200 is when a majority of the "late-game" Maplestory content is unlocked.
At Level 200, you unlock a new area accessible on your map called "Arcane River". You can access it through the drop down in the top left as if you were going to Grandis (Heliseum, etc).
[ Arcane River ]
---------------
There are currently 6 zones in Arcane River.
In order of level, the zones are: Vanishing Journey, Chu Chu Island, Lachelein, Arcana, Morass, and then Esfera.
You unlock Vanishing Journey at level 200, ChuChu at level 210, Lachelein at 220, Arcana at 225, Morass at 230, and Esfera at 235.
Each zone has it's own pre-quests before you can get their respective "Arcane Symbols".
[ Arcane Symbols]
-----------------
Arcane Symbols are in-essence additional stats to help you progress. It works much like star force where maps had requirements.
For arcane force, every map requires a certain amount for you to do full damage to the monsters there.
It's important to do your arcane river dailies every day for each zone to maximize your arcane force.```"""

def setup(client):
    client.add_cog(strings(client))
