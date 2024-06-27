import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.API_ID = os.getenv("API_ID")
        self.API_HASH = os.getenv("API_HASH")
        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        self.DB_NAME = os.getenv("DB_NAME", "terabox_links.db")
        self.MAX_CONCURRENT_DOWNLOADS = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", 5))
        self.BOT_USERNAME = os.getenv("BOT_USERNAME")
        self.DUMMY_ID = os.getenv("DUMMY_ID")

def load_config():
    config = Config()
    # Debug prints
    print(f"Loaded Config: API_ID={config.API_ID}, API_HASH={config.API_HASH}, BOT_TOKEN={config.BOT_TOKEN}, DB_NAME={config.DB_NAME}, MAX_CONCURRENT_DOWNLOADS={config.MAX_CONCURRENT_DOWNLOADS}, BOT_USERNAME={config.BOT_USERNAME}, DUMMY_ID={config.DUMMY_ID}")
    return config
