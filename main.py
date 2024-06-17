import random
import webbrowser



episode_titles = {
    1: {
        1: "Slumber Party Panic", 2: "Trouble in Lumpy Space", 3: "Prisoners of Love", 4: "Tree Trunks",
        5: "The Enchiridion!", 6: "The Jiggler", 7: "Ricardio the Heart Guy", 8: "Business Time",
        9: "My Two Favorite People", 10: "Memories of Boom Boom Mountain", 11: "Wizard", 12: "Evicted!",
        13: "City of Thieves", 14: "The Witch's Garden", 15: "What is Life?", 16: "Ocean of Fear",
        17: "When Wedding Bells Thaw", 18: "Dungeon", 19: "The Duke", 20: "Freak City",
        21: "Donny", 22: "Henchman", 23: "Rainy Day Daydream", 24: "What Have You Done?",
        25: "His Hero", 26: "Gut Grinder"
    },
    2: {
        1: "It Came from the Nightosphere", 2: "The Eyes", 3: "Loyalty to the King", 4: "Blood Under the Skin",
        5: "Storytelling", 6: "Slow Love", 7: "Power Animal", 8: "Crystals Have Power",
        9: "The Other Tarts", 10: "To Cut a Woman's Hair", 11: "The Chamber of Frozen Blades",
        12: "Her Parents", 13: "The Pods", 14: "The Silent King", 15: "The Real You",
        16: "Guardians of Sunshine", 17: "Death in Bloom", 18: "Susan Strong", 19: "Mystery Train",
        20: "Go With Me", 21: "Belly of the Beast", 22: "The Limit", 23: "Video Makers",
        24: "Heat Signature", 25: "Mortal Folly", 26: "Mortal Recoil"
    },
    3: {
        1: "Conquest of Cuteness", 2: "Morituri Te Salutamus", 3: "Memory of a Memory", 4: "Hitman",
        5: "Too Young", 6: "The Monster", 7: "Still", 8: "Wizard Battle",
        9: "Fionna and Cake", 10: "What Was Missing", 11: "Apple Thief", 12: "The Creeps",
        13: "From Bad to Worse", 14: "Beautopia", 15: "No One Can Hear You", 16: "Jake vs. Me-Mow",
        17: "Thank You", 18: "The New Frontier", 19: "Holly Jolly Secrets Part I",
        20: "Holly Jolly Secrets Part II", 21: "Marceline's Closet", 22: "Paper Pete",
        23: "Another Way", 24: "Ghost Princess", 25: "Dad's Dungeon", 26: "Incendium"
    },
    4: {
        1: "Hot to the Touch", 2: "Five Short Graybles", 3: "Web Weirdos", 4: "Dream of Love",
        5: "Return to the Nightosphere", 6: "Daddy's Little Monster", 7: "In Your Footsteps",
        8: "Hug Wolf", 9: "Princess Monster Wife", 10: "Goliad", 11: "Beyond this Earthly Realm",
        12: "Gotcha!", 13: "Princess Cookie", 14: "Card Wars", 15: "Sons of Mars",
        16: "Burning Low", 17: "BMO Noire", 18: "King Worm", 19: "Lady & Peebles",
        20: "You Made Me", 21: "Who Would Win", 22: "Ignition Point", 23: "The Hard Easy",
        24: "Reign of Gunters", 25: "I Remember You", 26: "The Lich"
    },
    5: {
        1: "Finn the Human", 2: "Jake the Dog", 3: "Five More Short Graybles", 4: "Up a Tree",
        5: "All the Little People", 6: "Jake the Dad", 7: "Davey", 8: "Mystery Dungeon",
        9: "All Your Fault", 10: "Little Dude", 11: "Bad Little Boy", 12: "Vault of Bones",
        13: "The Great Bird Man", 14: "Simon & Marcy", 15: "A Glitch is a Glitch",
        16: "Puhoy", 17: "BMO Lost", 18: "Princess Potluck", 19: "James Baxter the Horse",
        20: "Shh!", 21: "The Suitor", 22: "The Party's Over, Isla de Señorita", 23: "One Last Job",
        24: "Another Five More Short Graybles", 25: "Candy Streets", 26: "Wizards Only, Fools",
        27: "Jake Suit", 28: "Be More", 29: "Sky Witch", 30: "Frost & Fire",
        31: "Too Old", 32: "Earth & Water", 33: "Time Sandwich", 34: "The Vault",
        35: "Love Games", 36: "Dungeon Train", 37: "Box Prince", 38: "Red Starved",
        39: "We Fixed a Truck", 40: "Play Date", 41: "The Pit", 42: "James", 43: "Root Beer Guy",
        44: "Apple Wedding", 45: "Blade of Grass", 46: "Rattleballs", 47: "The Red Throne",
        48: "Betty", 49: "Bad Timing", 50: "Lemonhope Part 1", 51: "Lemonhope Part 2",
        52: "Billy's Bucket List"
    },
    6: {
        1: "Wake Up", 2: "Escape from the Citadel", 3: "James II", 4: "The Tower",
        5: "Sad Face", 6: "Breezy", 7: "Food Chain", 8: "Furniture & Meat",
        9: "The Prince Who Wanted Everything", 10: "Something Big", 11: "Little Brother",
        12: "Ocarina", 13: "Thanks for the Crabapples, Giuseppe!", 14: "Princess Day",
        15: "Nemesis", 16: "Joshua and Margaret Investigations", 17: "Ghost Fly",
        18: "Everything's Jake", 19: "Is That You?", 20: "Jake the Brick", 21: "Dentist",
        22: "The Cooler", 23: "The Pajama War", 24: "Evergreen", 25: "Astral Plane",
        26: "Gold Stars", 27: "The Visitor", 28: "The Mountain", 29: "Dark Purple",
        30: "The Diary", 31: "Walnuts & Rain", 32: "Friends Forever", 33: "Jermaine",
        34: "Chips and Ice Cream", 35: "Graybles 1000+", 36: "Hoots", 37: "Water Park Prank",
        38: "You Forgot Your Floaties", 39: "Be Sweet", 40: "Orgalorg", 41: "On the Lam",
        42: "Hot Diggity Doom", 43: "The Comet"
    },
    7: {
        1: "Bonnie & Neddy", 2: "Varmints", 3: "Cherry Cream Soda", 4: "Mama Said",
        5: "Football", 6: "Marceline The Vampire Queen", 7: "Everything Stays",
        8: "Vamps About", 9: "The Empress Eyes", 10: "May I Come In?", 11: "Take Her Back",
        12: "Checkmate", 13: "The Dark Cloud", 14: "The More You Moe, The Moe You Know (Part I)",
        15: "The More You Moe, The Moe You Know (Part II)", 16: "Summer Showers", 17: "Angel Face",
        18: "President Porpoise is Missing!", 19: "Blank-Eyed Girl", 20: "Bad Jubies",
        21: "King's Ransom", 22: "Scamps", 23: "Crossover", 24: "The Hall of Egress",
        25: "Flute Spell", 26: "The Thin Yellow Line", 27: "Broke His Crown", 28: "Don't Look",
        29: "Beyond the Grotto", 30: "Lady Rainicorn of the Crystal Dimension", 31: "I Am a Sword",
        32: "Bun Bun", 33: "Normal Man", 34: "Elemental", 35: "Five Short Tables",
        36: "The Music Hole", 37: "Daddy-Daughter Card Wars", 38: "Preboot", 39: "Reboot"
    },
    8: {
        1: "Two Swords", 2: "Do No Harm", 3: "Wheels", 4: "High Strangeness", 5: "Horse and Ball",
        6: "Jelly Beans Have Power", 7: "Islands Part 1: The Invitation", 8: "Islands Part 2: Whipple the Happy Dragon",
        9: "Islands Part 3: Mysterious Island", 10: "Islands Part 4: Imaginary Resources", 11: "Islands Part 5: Hide and Seek",
        12: "Islands Part 6: Min and Marty", 13: "Islands Part 7: Helpers", 14: "Islands Part 8: The Light Cloud",
        15: "Orb", 16: "Elements Part 1: Skyhooks", 17: "Elements Part 2: Bespoken For", 18: "Elements Part 3: Winter Light",
        19: "Elements Part 4: Cloudy", 20: "Elements Part 5: Slime Central", 21: "Elements Part 6: Happy Warrior",
        22: "Elements Part 7: Hero Heart", 23: "Elements Part 8: Skyhooks II", 24: "Abstract", 25: "Ketchup",
        26: "Fionna and Cake and Fionna", 27: "Whispers", 28: "Three Buckets"
    },
    9: {
        1: "Orb", 2: "The Wild Hunt", 3: "Always BMO Closing", 4: "Son of Rap Bear",
        5: "Bonnibel Bubblegum", 6: "Seventeen", 7: "Ring of Fire", 8: "Marcy & Hunson",
        9: "The First Investigation", 10: "Blenanas", 11: "Jake the Starchild", 12: "Temple of Mars",
        13: "Gumbaldia", 14: "Come Along With Me"
    },
    10: {
        1: "The Wild Hunt", 2: "Always BMO Closing", 3: "Son of Rap Bear", 4: "Bonnibel Bubblegum",
        5: "Seventeen", 6: "Ring of Fire", 7: "Marcy & Hunson", 8: "The First Investigation",
        9: "Blenanas", 10: "Jake the Starchild", 11: "Temple of Mars", 12: "Gumbaldia",
        13: "Come Along With Me"
    }
}
print("Welcome to the Adventure Time Episode Randomizer!")

# Prompt the user for a specific season or the whole show
input_season = input("Enter a season number (1-10) or 'all' for the whole show: ")

if input_season == "all":
    # Randomly select a season and episode
    season = random.choice(list(episode_titles.keys()))
    episode = random.choice(list(episode_titles[season].keys()))
    print(f"Season {season}, Episode {episode}: {episode_titles[season][episode]}")
else:
    # Convert the input to an integer
    season = int(input_season)
    # Randomly select an episode from the specified season
    episode = random.choice(list(episode_titles[season].keys()))
    print(f"Season {season}, Episode {episode}: {episode_titles[season][episode]}")

# Open a specific webpage
webpage_url = f"https://www.braflix.ru/tv/15260/{season}/{episode}?play=true"
webbrowser.open(webpage_url)
