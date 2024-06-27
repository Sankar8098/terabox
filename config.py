import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.API_ID = os.getenv("23990433")
        self.API_HASH = os.getenv("e6c4b6ee1933711bc4da9d7d17e1eb20")
        self.BOT_TOKEN = os.getenv("6662329787:AAHUuH45cuvNfBj_pzd5LO5Q8N50N3h5lCw")
        self.DB_NAME = os.getenv("DB_NAME", "terabox_links.db")
        self.MAX_CONCURRENT_DOWNLOADS = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", 5))
        self.BOT_USERNAME = os.getenv("SKAutoApprovalbot")
        self.DUMMY_ID = os.getenv("5821871362")

def load_config():
    config = Config()
    # Debug prints
    print(f"Loaded Config: API_ID={config.API_ID}, API_HASH={config.API_HASH}, BOT_TOKEN={config.BOT_TOKEN}, DB_NAME={config.DB_NAME}, MAX_CONCURRENT_DOWNLOADS={config.MAX_CONCURRENT_DOWNLOADS}, BOT_USERNAME={config.BOT_USERNAME}, DUMMY_ID={config.DUMMY_ID}")
    return config
