import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import start, handle_message, save_phone
from bot.file_handler import handle_document, handle_photo
from bot.websearch import web_search
from bot.config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def main():
    try:
        app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("websearch", web_search))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.add_handler(MessageHandler(filters.CONTACT, save_phone))
        app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
        app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

        print("✅ Bot is running...")
        app.run_polling()

    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == "__main__":
    main()
