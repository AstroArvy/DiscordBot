# This script creates and sends an embeded message to the discord server channel. 

import discord
import os
from dotenv import load_dotenv

# Create a bot instance with the specified intents

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Embed bot running')

# Function to send an embed message
async def send_custom_embed(channel, title, description, color, thumbnail_url):
    # Create an embed object
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    # Set the thumbnail image
    embed.set_thumbnail(url=thumbnail_url)

    # Send the embed message
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('BacPacTeam'):
        # Founder 1
        await send_custom_embed(
            message.channel,
            title='Founder CEO' + ' ' * 50,
            description='Aryan Bansal',
            color=0x00FFFF,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Founder 2
        await send_custom_embed(
            message.channel,
            title='Founder COO    ',
            description='Sukhwan Jeong',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Founder 3
        await send_custom_embed(
            message.channel,
            title='Founder CPO    ',
            description='Joohyun Park',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Founder 4
        await send_custom_embed(
            message.channel,
            title='Founder CTO    ',
            description='Utkarsh Gupta',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Designer 1
        await send_custom_embed(
            message.channel,
            title='Designer',
            description='Anirudha \n Bhalashankar',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Developer 1
        await send_custom_embed(
            message.channel,
            title='Developer',
            description='Satyam \n Kumar',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )

        # Developer 2
        await send_custom_embed(
            message.channel,
            title='Developer',
            description='Meenal \n Nimje',
            color=0xFF0000,
            thumbnail_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwIg8kzW53TaVy4F9BokCIf6DSWyK3tnq5q_MIYFxxjGA0UGcDa4cJisFDdC85oOFGr1Q&usqp=CAU'
        )

        # Developer 3
        await send_custom_embed(
            message.channel,
            title='Developer',
            description='Ayush \n Tiwari',
            color=0xFF0000,
            thumbnail_url='https://pbs.twimg.com/profile_images/1681432518833352705/XnlIAyHt_400x400.jpg'
        )
