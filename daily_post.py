import discord
import requests
import random
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import datetime

# Load environment variables from a .env file
load_dotenv()

UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")

# Define your bot's prefix (e.g., "!cute") and create an instance of the bot
bot = commands.Bot(command_prefix="!cute", intents = discord.Intents.all())


# Define the channels for different content
channels = {
    "animal-lovers": "cute pet closeup",
    "science":"cosmos, universe",
    "arts":"painting"
}

# Function to fetch a random photo URL from Unsplash based on a keyword
def fetch_random_unsplash_photo(keyword):
    api_url = "https://api.unsplash.com/photos/random"
    params = {
        "query": keyword,
        "orientation": "landscape",
    }
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_API_KEY}",
    }
    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["urls"]["regular"]
    else:
        return None

@bot.event
async def on_ready():
    print("Daily bot running")

@tasks.loop(hours=24)  # Set the loop to run every 24 hours
async def post_content():
    for channel_name, keyword in channels.items():
        photo_url = fetch_random_unsplash_photo(keyword)
        print(photo_url)
        if photo_url:
            embed = discord.Embed()
            embed.set_image(url=photo_url)
            for guild in bot.guilds:
                channel = discord.utils.get(guild.text_channels, name=channel_name)
                print(channel)
                if channel:
                    await channel.send(embed=embed)


@bot.event
async def on_ready():
    print("Daily Bot running")
    post_content.start()
