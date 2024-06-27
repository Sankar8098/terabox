import tracemalloc
import asyncio
from pyrogram import Client
from config import load_config
from handlers import register_handlers
from database import init_database
from utils.logging import setup_logger
from browser.fetch_videos import init_session, close_session

tracemalloc.start()

async def main():
    config = load_config()
    logger = setup_logger()

    # Debug prints to verify configuration loading
    print(f"API_ID: {config.API_ID}")
    print(f"API_HASH: {config.API_HASH}")
    print(f"BOT_TOKEN: {config.BOT_TOKEN}")
    print(f"DB_NAME: {config.DB_NAME}")
    print(f"MAX_CONCURRENT_DOWNLOADS: {config.MAX_CONCURRENT_DOWNLOADS}")
    print(f"BOT_USERNAME: {config.BOT_USERNAME}")
    print(f"DUMMY_ID: {config.DUMMY_ID}")

    app = Client(
        "terabox_downloader",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN
    )

    client_started = False
    try:
        await init_database()
        await init_session(max_concurrent_downloads=config.MAX_CONCURRENT_DOWNLOADS)
        register_handlers(app)

        await app.start()
        client_started = True
        logger.info("Bot started successfully")
        await asyncio.Future()  # This replaces idle()
    except Exception as e:
        logger.error(f"Error in main function: {e}")
    finally:
        if client_started:
            await app.stop()
        await close_session()

if __name__ == "__main__":
    asyncio.run(main())
