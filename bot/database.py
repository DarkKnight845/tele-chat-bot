import os
import logging
from pymongo import MongoClient
from urllib.parse import quote_plus

# Configur elogging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


try:
    # TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
    # GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
    username = os.environ["MONGO_USERNAME"]
    password = os.environ["MONGO_PASSWORD"]
    cluster = os.environ["MONGO_CLUSTER"]
    db_name = os.environ["MONGO_DB_NAME"]
    MONGO_URI = os.environ["MONGO_URI"]

    # URL-encode the username and password to escape special characters
    # username = quote_plus(username)
    password = quote_plus(password)

    MONGO_URI = f"mongodb+srv://ayemiade2020:{password}@cluster0.rwbpt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["telegram_ai_bot"]

    # collections
    users_collection = db["users"]
    chats_collection = db["chat_history"]
    files_collection = db["file_metadata"]

    print("✅ Connected to MongoDB successfully!")


except KeyError as e:
    logger.error(f"❌ Missing environment variable: {e}")
    # Checking for missing values
    raise ValueError("❌ Missing required environment variables!")

except Exception as e:
    logger.error(f"❌ Error connecting to MongoDB: {e}")
    raise

    
print("✅ Environment variables loaded successfully!")

