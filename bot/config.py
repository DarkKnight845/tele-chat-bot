import os
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Load environment variables using os.environ
    MONGO_URI = os.environ["MONGO_URI"]
    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
    TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

    print("✅ Environment variables loaded successfully!")

except KeyError as e:
    logger.error(f"❌ Missing required environment variable: {e}")
    raise ValueError(f"Missing required environment variable: {e}")

except Exception as e:
    logger.error(f"❌ Error loading environment variables: {e}")
    raise
