import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from bot.database import users_collection, chats_collection
from bot.gemini import get_gemini_response

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    try:
        user = update.effective_user
        chat_id = update.effective_chat.id

        # save user info if they are new
        if not users_collection.find_one({"chat_id": chat_id}):
            users_collection.insert_one({"chat_id": chat_id, "username": user.username, "first_name":user.first_name})
        
        # request phone number
        keyboard = [[KeyboardButton("📞 Share Phone Number", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text("Welcome! Please share your phone number", reply_markup=reply_markup)

    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await update.message.reply_text("❌ An error occurred. Please try again")

async def save_phone(update: Update, context: CallbackContext) -> None:
    try:
        contact = update.message.contact
        chat_id = update.effective_chat.id

        users_collection.update_one({"chat_id": chat_id}, {"$set": {"phone_number": contact.phone_number}})
        await update.message.reply_text("✅ Phone number saved successfully!")

    except Exception as e:
        logger.error(f"Error saving phone number: {e}")
        await update.message.reply_text("❌ Failed to save phone number")

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        user_text = update.message.text
        chat_id = update.effective_chat.id

        response = get_gemini_response(user_text)
        chats_collection.insert_one({"chat_id": chat_id, "user_input": user_text, "bot_response": response})

        await update.message.reply_text(response)
    
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await update.message.reply_text("❌ I encountered an error. Try again later.")