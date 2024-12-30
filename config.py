# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "26107399")
    API_HASH = os.environ.get("API_HASH", "e10525d8ad0189f8bf7a82a32f538d12")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Arravk:AYUSHRAJ@cluster0.imq86.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '1685470205').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
