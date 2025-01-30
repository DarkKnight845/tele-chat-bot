import logging
from telegram import Update
from telegram.ext import CallbackContext
from bot.database import files_collection
from bot.gemini import get_gemini_response

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

async def handle_document(update: Update, context: CallbackContext) -> None:
    try:
        file = update.message.document
        file_id = file.file_id
        file_name = file.file_name
        chat_id = update.effective_chat.id

        files_collection.insert_one({"chat_id": chat_id, "file_id": file_id, "file_name": file_name})
        await update.message.reply_text(f"✅ Received file: {file_name}")

    except Exception as e:
        logger.error(f"Error handling document: {e}")
        await update.message.reply_text("❌ Failed to process the file.")

async def handle_photo(update: Update, context: CallbackContext) -> None:
    try:
        photo = update.message.photo[-1]  # Get highest resolution
        file_id = photo.file_id
        chat_id = update.effective_chat.id

        response = get_gemini_response("Describe this image")
        files_collection.insert_one({"chat_id": chat_id, "file_id": file_id, "description": response})
        
        await update.message.reply_text(f"📸 Image Analysis:\n{response}")

    except Exception as e:
        logger.error(f"Error handling photo: {e}")
        await update.message.reply_text("❌ Failed to analyze the image.")
