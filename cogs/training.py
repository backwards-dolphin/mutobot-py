import discord
from discord.ext import commands

spots = {10: "Green Mushroom: Henesys: Spore Hill",
15: "Stone Golem - Henesys: Golem’s Temple Entrance",
19: "Flaming Mixed Golem - Henesys: Golem Temple 3",
26: "Evil eyes - North Forest: Giant Tree",
27: "Curse Eye - North Forest: Green Tree Trunk",
33: "Grumpy Tome - Ellinel Academy: Second Floor: Library",
35: "Coconut Slimes - Gold Beach: Beachgrass Dunes 1",
36: "Violet Clam Slime - Gold Beach: Seaside 2",
41: "Starfish Octopus - Gold Beach: Gentle Waves 2",
42: "Seashell Octopus Slime - Gold Beach: Hardwave Beach",
52: "Polluter Barrel, Corrupter Barrels - Riena Strait: Polluted Glacier 2",
53: "Possibly-Evil Seal - Riena Strait: Underwater Ice Cave",
55: "Wild Boar - Perion: Wild Boar Land",
60: "Mushroom Chandelier - Mushroom Castle: Castle Corridor",
62: "Skeledog - Perion: Military Camp 1",
65: "Master Squid - Mushroom Castle: Viking Airship: Galley",
66: "Copper Drake - Sleepywood: Silent Swamp",
71: "Grupin, Cellion, Lioner - Orbis: Stairway to the Sky 1",
81: "White Fang - El Nath: Ice Valley II",
86: "Desert Rabbit(F) - Nihal Desert: Outside Far Entrance of Ariant",
89: "Sand Rat - Nihal Desert: The Desert of Serenity\nSand Rat & Scorpion - Ariant: Sahel 2",
95: "Neo Huroid - Magatia: Lab - Area C-3\nRoid - Magatia: Lab  -  Area C - 1",
103: "Rash - Leafre: West Leafre Forest",
104: "Warrior Spectre - Tyrant's Castle: Tyrant's Castle 2nd/3rd Floor Mezzanine",
110: "Normal Zakum (Arms) - Dead Mine: Entrance to Zakum",
113: "Toy Trojan - Ludibrium: Sky Terrace<5>\nRobo - Ludibrium: Toy Factory <Process 1> Zone 5\nRobo & Master Robo - Ludibrium: Toy Factory <Apparatus Room>",
119: "Ghost Pirate(*26) - Ludibrium: Warped Path of Time<3>",
126: "Straw Target Dummy - Mu Lung Garden: Practice Field: Easy Level",
130: "Kru - Herb Town: Red-Nose Pirate Den 3\nMoon Bunny - Korean Folk Town: Black Mountain Entrance",
136: "Bain[*55] - El Nath: The Cave of Trials III",
140: "Yellow King Goblin - Korean Folk Town: Goblin House",
141: "Dark Wyvern[*65] - Minar Forest: Black Wyvern's Nest",
155: "Flora - Stone Colossus: Colossus East Road 2\n[*80]Enraged Espresso Machine - Kerning Tower: 2F Cafe <4>",
160: "Normal Horntail - Leafre: Cave of Life",
161: "Deadly Dressing Table[*80] - Kerning Tower: 5F Cosmetics Shops <4>",
162: "Mutant Snail - Henesys Ruins: Henesys Ruins Market",
164: "Oblivion Guardian - Temple of Time: Time Lane: Road to Oblivion 4\nOblivion Guardian[*90] - Temple of Time: Time Lane: Detour to Oblivion 4",
170: "Official Knight A, B, C - Knight Stronghold: Knight District 1-2",
173: "Gray Commuter Saucer - Omega Sector: Corridor 204",
175: "Gray Luxury Saucer - Omega Sector: Corridor 202",
178: "Gray Commuter Saucer[*140] - Omega Sector: Corridor H01",
184: "Advanced Knight A-E - Knight Stronghold: Hall of Honor",
190: "Swollen Stump - Twilight Perion: Desolate Hills\nSwollen Stump - Twilight Perion: Deserted Southern Ridge",
195: "Sinister Rocky Mask - Twilight Perion: Forsaken Excavation Site 2",
196: "Sinister Steel Mask - Twilight Perion: Forsaken Excavation Site 4",
201: "Raging Erda[x30] - Vanishing Journey: Weathered Land of Rage",
205: "Blazing Erda[x40] - Vanishing Journey: Fire Zone",
208: "Chaseroid Blue - Scrapyard: Scrapyard Hill 5",
207: "Tranquil & Lantern Erda[x60] - Vanishing Journey: Cave Path 2",
213: "Angry Flyon & Ripe Wolfruit[x100] - Chu Chu Island: Slurpy Forest Depths",
215: "Rhyturtle & Boss Rhyturtle[x130] - Chu Chu Island: Torrent Zone 3",
222: "Gallus[x210] - Lachelein: Chicken Festival 2",
223: "Angry & Insane Masquerade Citizen[x210] - Lachelein: Revelation Place 3",
226: "Dreamkeeper[x240] - Lachelein: Nightmare Clocktower 2F",
232: "Earth Spirit[x280] - Arcana: The Forest of Earth",
233: "Snow & Thunder Cloud Spirit[x320] - Arcana: Between Frost and Thunder 2",
236: "Xenoroid Echo Type B[x400] - Morass: Path to the Coral Forest 4",
237: "Befuddled Spirit[x360] - Arcana: Cavern Lower Path",
238: "Strong & Powerful Gangster[x440] - Morass: Bully Blvd. 2",
242: "Thralled Guard & Warhammer Knight[x520] - Morass: The Day in Trueffet 2"
    }

class training:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context = True)
    async def train(self, ctx, level, range = 7):
        try:
            iLvl = int(level)
            iRange = int(range)
        except:
            await self.client.say("Please enter numbers, not letters!")
            return
        # call dictionary for levels from strings.py and output results in discord format - embed maybe
        if iRange <= 20:
            string = ""
            embed=discord.Embed(title="Training spots", color=0xffdd88)
            embed.set_thumbnail(url="https://i.imgur.com/LpZoKi7.png")
            for key, value in spots.items():
                if iLvl - iRange < key < iLvl + iRange:
                    embed.add_field(name="Level " + str(key), value=value, inline=False)
            embed.set_footer(text="If you have training spot suggestions or find an error please contact @colin#0001")
            await self.client.say(embed=embed)
        else:
            await self.client.say("Please use a smaller range! (less than 20)")

def setup(client):
    client.add_cog(training(client))
