import discord
from discord.ext import commands
import random
from decimal import Decimal

#Establish arrays for success/maintain and fail rates
starToSuccess = {0: 0.95, 1: 0.9, 2: 0.85, 3: 0.85, 4: 0.8, 5: 0.75, 6: 0.7,
                 7: 0.65, 8: 0.6, 9: 0.55, 10: 0.45, 11: 0.35, 12: 0.30, 13: 0.30,
                 14: 0.30, 15: 0.30, 16: 0.30, 17: 0.30, 18: 0.30, 19: 0.30, 20: 0.30, 21: 30,
                 22: 0.03, 23: 0.02, 24: 0.01}

starToMaint = {0: 0.05, 1: 0.1, 2: 0.15, 3: 0.15, 4: 0.20, 5: 0.25, 6: 0,
                 7: 0, 8: 0, 9: 0, 10: 0.55, 11: 0, 12: 0, 13: 0,
                 14: 0, 15: 0.679, 16: 0, 17: 0, 18: 0, 19: 0, 20: 63, 21: 0,
                 22: 0, 23: 0, 24: 0}

starToDecrease = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0.3,
                 7: 0.35, 8: 0.40, 9: 0.45, 10: 0, 11: 0.65, 12: 0.6931, 13: 0.686,
                 14: 0.686, 15: 0, 16: 0.679, 17: 0.679, 18: 0.672, 19: 0.672, 20: 0, 21: 0.63,
                 22: 0.776, 23: 0.686, 24: 0.594}

class starsim:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def star(self, ctx, money: str, stars=22):
        moneyVals = []
        finalMoney = 0
        d = {'K': 3, 'M': 6, 'B': 9, 'k': 3, 'm': 6, 'b': 9}
        if money[-1] in d:
            num, magnitude = money[:-1], money[-1]
            finalMoney = Decimal(num) * 10 ** d[magnitude]
        else:
            finalMoney = Decimal(money)

        if stars > 22:
            self.client.say("Invalid star amount, please select 22* or below")
        else:
            totalDestroys = 0
            totalEnhance = 0
            for i in range (0, 1000):
                currentMoney = 0
                currentStars = 0
                while not currentStars == stars:
                    starSuccess = starToSuccess.get(currentStars)
                    starMaint = starToMaint.get(currentStars)
                    starDecrease = starToDecrease.get(currentStars)
                    output = random.random()
                    totalEnhance += 1
                    # Add money values based on a lv160 equip using KMS formulas
                    if 0 <= currentStars <= 9:
                        currentMoney += (1000 + (160 ** 3) * (currentStars + 1)/25)
                    elif 10 <= currentStars <= 14:
                        currentMoney += (1000 + (160 ** 3) * ((currentStars+1) ** 2.7) / 400)
                    else:
                        currentMoney += (1000 + (160 ** 3) * ((currentStars+1) ** 2.7) / 200)

                    if 0 < output <= starSuccess:
                        currentStars +=1
                    elif starSuccess < output < starMaint:
                        pass
                    elif starSuccess < output < starDecrease:
                        currentStars -= 1
                    elif starSuccess + starMaint + starDecrease <= output:
                        currentStars = 0
                        totalDestroys += 1
                moneyVals.append(currentMoney)

            total=0
            for num in moneyVals:
                if num <= finalMoney:
                    total+=1
            odds = total/1000
            embed=discord.Embed(title="Starring Simulation", color=0xffdd88)
            embed.set_thumbnail(url="https://i.imgur.com/LpZoKi7.png")
            embed.add_field(name="Stars", value=str(stars), inline=True)
            embed.add_field(name="Budget", value=money, inline=True)
            embed.add_field(name="Average enhancements", value=str(totalEnhance/1000), inline=True)
            embed.add_field(name="Average booms", value=str(totalDestroys/1000), inline=True)
            embed.add_field(name="Odds", value = str(odds),inline=True)
            await self.client.say(embed=embed)

    #Convert 100m/100b etc to number
    def convert(val):
        lookup = {'k': 1000, 'm': 1000000, 'b': 1000000000}
        unit = val[-1]
        try:
            number = int(val[:-1])
        except ValueError:
            print("Invalid entry")
        if unit in lookup:
            return lookup[unit] * number
        return int(val)


def setup(client):
    client.add_cog(starsim(client))
