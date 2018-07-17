def getHelp():
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

< Supported roles >
#hmag
#cvel
#notifications```"""
    return msg

def getCap():
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
    return msg

def getTrainDict():
    spots = {10: "[LV10]Green Mushroom: Henesys: Spore Hill",
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
    173: "Gray Commuter Saucer - Omega Sector: Corridor 204",
    175: "Gray Luxury Saucer - Omega Sector: Corridor 202",
    178: "Gray Commuter Saucer[*140] - Omega Sector: Corridor H01",
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
    return spots
