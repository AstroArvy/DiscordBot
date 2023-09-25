# run_bot.py

import asyncio
import os
from dotenv import load_dotenv
#from chatbot import client as chatbot_client
from message_embed import client as embed_client
from q_and_a import client as q_and_a_client
#from invite import client as invite_client
#from invite2 import bot as invite_bot
from daily_post import bot as daily_bot


# Load environment variables from a .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


if __name__ == "__main__":

    # Create and run separate event loops for each bot
    loop = asyncio.get_event_loop()
    #loop.create_task(chatbot_client.start(TOKEN))  # Run the chatbot
    #loop.create_task(invite_client.start(TOKEN))  # Run the embed message bot
    loop.create_task(embed_client.start(TOKEN))  # Run the embed message bot
    loop.create_task(q_and_a_client.start(TOKEN))  # Run the Q&A bot
    #loop.create_task(invite_bot.start(TOKEN))  # Run the embed message bot
    loop.create_task(daily_bot.start(TOKEN))  # Run the Q&A bot
    

    loop.run_forever()