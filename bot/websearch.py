import logging
from telegram import Update
from telegram.ext import CallbackContext

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

async def web_search(update: Update, context: CallbackContext) -> None:
    try:
        query = "".join(context.args)
        if not query:
            await update.message.reply_text("Usage: /websearch <query>")

    except Exception as e:
        logger.error(f"Error performing web search: {e}")
        await update.message.reply_text("❌ Failed to fetch search results.")