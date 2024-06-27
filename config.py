import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.API_ID = os.getenv("24444928")
        self.API_HASH = os.getenv("0a278a515cd13ec8802b7dabed73dede")
        self.BOT_TOKEN = os.getenv("7029092370:AAEhUE-EibLL1Akv26od7PCv0rqL1mXk_m0")
        self.DB_NAME = os.getenv("DB_NAME", "terabox_links.db")
        self.MAX_CONCURRENT_DOWNLOADS = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", 5))
        self.BOT_USERNAME = os.getenv("bot_username")
        self.DUMMY_ID = os.getenv("dummy_id")

def load_config():
    return Config()
