from pyrogram import Client
from pyrogram.raw.functions.messages import RequestWebView
from urllib.parse import unquote
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Credentials for the Telegram API
api_id = os.getenv('api_id')  # API ID from Telegram
api_hash = os.getenv('api_hash')  # API hash from Telegram
phone_number = os.getenv('phone_number')  # Your phone number registered with Telegram

# Target bot details (e.g., Hamster Kombat bot)
bot_username = 'hamster_kombat_bot'  # The bot's username
bot_url = 'https://hamsterkombatgame.io/'  # The URL to be requested via WebView

async def get_InitData():
    # Create a new Pyrogram client session
    client = Client('session', api_id, api_hash, phone_number=phone_number)

    # Use the client within the asynchronous context
    async with client:
        # Resolve the peer (the bot) to interact with it
        peer = await client.resolve_peer(bot_username)

        # Invoke a raw function to request a WebView from the bot
        web_view = await client.invoke(
            RequestWebView(
                peer=peer,  # The bot's peer
                bot=peer,  # The bot itself
                platform='android',  # Specify the platform (Android in this case)
                from_bot_menu=False,  # Indicates whether it's from a bot menu
                url=bot_url,  # URL to load in the WebView
            )
        )

        # Extract the URL returned by the WebView
        auth_url = web_view.url

        # Parse and decode the 'InitData' from the URL query parameters
        initData = unquote(
            string=auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0]
        )

        # Return the extracted InitData
        return initData

# Run the asynchronous function to get InitData and print it
initData = asyncio.run(get_InitData())
print(initData)
