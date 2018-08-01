import discord
from discord.ext import commands
import shelve
import os

bosses = ["damien", "lotus", "cvel", "3door", "hmag", "lucid"]
image = {"damien": "https://i.imgur.com/XlDxegv.png", "lotus": "https://i.imgur.com/JBLhwgx.png",
"hmag": "https://i.imgur.com/CXWxoSk.png", "lucid": "https://i.imgur.com/DHGqVpM.png", "cvel": "https://i.imgur.com/kVFEEh5.png", "3door": "https://i.imgur.com/kVFEEh5.png"}
owner = ["89973782285910016"]

class bossqueue:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def queue(self, ctx, boss):
        if boss in bosses:
            sBoss = shelve.open("boss", flag='c', writeback=True)
            if boss not in sBoss:
                sBoss[boss] = [ctx.message.author.name]
                await self.client.say("I've added you to the queue, {0}".format(ctx.message.author.mention))
                sBoss.close()
            else:
                sBoss[boss].append(ctx.message.author)
                await self.client.say("I've added you to the queue, {0}".format(ctx.message.author.mention))
                sBoss.close()
        else:
            await self.client.say("Invalid boss. Please use the bosses from .help")

    @commands.command(pass_context=True)
    async def list(self, ctx, boss):
        if boss in bosses:
            sBoss=shelve.open('boss', flag='c')
            if boss in sBoss:
                embed=discord.Embed(title="Boss Partying", color=0xffdd88)
                embed.set_thumbnail(url=image.get(boss))
                names = ""
                for name in sBoss[boss]:
                    names += name + "\n"
                names = names[:-1]
                embed.add_field(name=names,value='\u200b', inline=True)
                sBoss.close()
                await self.client.say(embed=embed)
            else:
                await self.client.say("There is no one in queue.")
        else:
            await self.client.say("Invalid boss. Please use the bosses from .help")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True)
    async def refresh(self, ctx, boss="all"):
        sBoss = shelve.open("boss", flag='c')
        sBoss.clear()
        if boss == "all":
            sBoss["damien"] = []
            sBoss["lotus"] = []
            sBoss["lucid"] = []
            sBoss["3door"] = []
            sBoss["hmag"] = []
            sBoss["cvel"] = []
            await self.client.say("I've cleared all lists!")
        else:
            if boss in bosses:
                sBoss[boss] = []
                await self.client.say("I've cleared {0}!".format(boss))
        sBoss.close()

    @commands.command(pass_context=True)
    async def removefiles(self, ctx):
        if ctx.message.author.id in owner:
            os.remove("boss.bak")
            os.remove("boss.dat")
            os.remove("boss.dir")
            await self.client.say("Files removed")
        else:
            await self.client.say("You are missing permissions!")

def setup(client):
    client.add_cog(bossqueue(client))
