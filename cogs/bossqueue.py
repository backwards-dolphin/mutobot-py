import discord
from discord.ext import commands
from os import environ
from firebase import firebase

bosses = ["damien", "lotus", "cvel", "3door", "hmag", "lucid"]
image = {"damien": "https://i.imgur.com/XlDxegv.png", "lotus": "https://i.imgur.com/JBLhwgx.png",
"hmag": "https://i.imgur.com/CXWxoSk.png", "lucid": "https://i.imgur.com/DHGqVpM.png", "cvel": "https://i.imgur.com/kVFEEh5.png",
"3door": "https://i.imgur.com/Gg6Ys8B.png"}
name = environ['url']
url = "https://" + str(name) + ".firebaseio.com/"

class bossqueue:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def queue(self, ctx, boss):
        if boss in bosses:
            fb = firebase.FirebaseApplication(url, None)
            result = fb.get('/{0}/{1}'.format(boss, ctx.message.author.id), None)
            if result != None:
                await self.client.say("You're already queued for this boss.")
                return
            append = fb.patch('/{0}/'.format(boss), {ctx.message.author.id: ctx.message.author.display_name})
            try:
                newRank = discord.utils.get(ctx.message.server.roles, name="{0}".format(boss.tolower()))
                await client.add_roles(ctx.message.author, newRank)
            except:
                print("this don't work!!!!")

            await self.client.say("I've added you to the queue and role, {0}".format(ctx.message.author.mention))
        else:
            await self.client.say("Invalid boss. Please use the bosses from .help")

    @commands.command(pass_context=True)
    async def unqueue(self, ctx, boss):
        if boss.lower() in bosses:
            fb = firebase.FirebaseApplication(url, None)
            result = fb.get('/{0}'.format(boss), None)
            if result != None:
                try:
                    for key in result:
                        if key == ctx.message.author.id:
                            fb.delete('/{0}'.format(boss), ctx.message.author.id)
                            try:
                                newRank = discord.utils.get(ctx.message.server.roles, name="{0}".format(boss.tolower()))
                                await client.remove_roles(ctx.message.author, newRank)
                            except:
                                print("this don't work!!!!")
                            await self.client.say("I've removed you from the list.")
                except:
                    await self.client.say("You are not queued for this boss.")


    @commands.command(pass_context=True)
    async def list(self, ctx, boss):
        if boss.lower() in bosses:
            fb = firebase.FirebaseApplication(url, None)
            result = fb.get('/{0}/'.format(boss), None)
            if result != None:
                names=""
                for key in result:
                    name = fb.get('/{0}/{1}'.format(boss, key), None) + "\n"
                    names += name
                embed=discord.Embed(title="Boss Partying", color=0xffdd88)
                embed.set_thumbnail(url=image.get(boss))
                if names != "":
                    embed.add_field(name=names,value='\u200b', inline=True)
                    await self.client.say(embed=embed)
            else:
                await self.client.say("There is no one in queue.")
        else:
            await self.client.say("Invalid boss. Please use the bosses from .help")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True)
    async def refresh(self, ctx, boss="all"):
        fb = firebase.FirebaseApplication(url, None)
        if boss == "all":
            for allBoss in bosses:
                result = fb.get('/{0}/'.format(allBoss), None)
                if result != None:
                    for key in result:
                        fb.delete('/{0}'.format(allBoss), key)
            await self.client.say("I've refreshed all bosses.")
        elif boss.lower() in bosses:
            result = fb.get('/{0}/'.format(boss), None)
            for key in result:
                fb.delete('/{0}'.format(boss), key)
            await self.client.say("I've refreshed {0}".format(boss))
        else:
            await self.client.say("Invalid Boss.")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx, user, boss):
        if boss.lower() in bosses:
            fb = firebase.FirebaseApplication(url, None)
            result = fb.get('/{0}/'.format(boss), None)
            if result != None:
                for key in result:
                    name = fb.get('/{0}/{1}'.format(boss, key), None)
                    if user in name:
                        fb.delete('/{0}'.format(boss), key)
                        await self.client.say("I've deleted this user.")
                        return
            await self.client.say("User not found in boss.")
        else:
            await self.client.say("Invalid Boss.")

    async def carry_notifications(self):
        carries = discord.Object(id='408139117944242176')
        count = 0
        embed=discord.Embed(title="Daily boss reminder", color=0xffdd88)
        fb = firebase.FirebaseApplication(url, None)
        for boss in bosses:
            names = ""
            result = fb.get('/{0}/'.format(boss), None)
            if result != None:
                for key in result:
                    name = fb.get('/{0}/{1}'.format(boss, key), None)
                    names += name + ", "
                names = names[:-1]
                embed.add_field(name=boss.capitalize() + " (" + str(len(result)) + ")",value=names, inline=False)
            else:
                count+=1
        if count != len(bosses):
            await self.client.send_message(carries,embed=embed)


def setup(client):
    client.add_cog(bossqueue(client))
