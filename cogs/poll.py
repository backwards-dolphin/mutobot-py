import discord
from discord.ext import commands
class poll:
    def __init__(self,client):
        self.client = client

    @commands.has_permissions(manage_roles = True)
    @commands.command(pass_context=True)  # Taken from github/Vexs but formatted
    async def poll(self, ctx, *, options: str):

        list1 = options.split("|")
        question = list1[0] # Get the question
        entries = list1[1:] # Get the answers

        if len(entries) <= 1:
            await self.client.say('You need more than one option to make a poll!')
            return
        if len(entries) > 11:
            await self.client.say('You cannot make a poll for more than 10 things!')
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
        react_message = await self.client.say(embed=embed)
        for reaction in reactions[:len(entries)]:
            await self.client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await self.client.edit_message(react_message, embed=embed)

def setup(client):
    client.add_cog(poll(client))
