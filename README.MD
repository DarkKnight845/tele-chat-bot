# Tele Chat Bot

## Overview

Tele Chat Bot is a versatile and user-friendly chatbot designed to facilitate seamless communication on Telegram. It offers a range of features to enhance user interaction and automate tasks, making it an essential tool for both personal and professional use.

## Features

- **Easy Setup**: Quick and straightforward installation process.
- **Customizable**: Tailor the bot's responses and functionalities to suit your needs.
- **Secure**: Ensures user data privacy and security.
- **Scalable**: Capable of handling multiple users and conversations simultaneously.

Explore the capabilities of Tele Chat Bot and streamline your Telegram communication experience.

## Key Components of the Chat Bot
1. User Registeration: Saves the first name, username and chat ID in MongoDB upon first interaction. It also requests and stores the user's phone number
2. AI-Powered Chat: uses Google Gemini API to respond to user queries. Stores full chat hiistoryb in MongoDB with timestamps.
3. Image and File Analysis: Accepts images/files (JPG, PNG, PDF) and analyzes content using Gemini. Replies with analysis and saves file metadata in MongoDB.
4. Web Search: Users can perform a web  search by entering a query. The bot fetches summarized AI-generated results along with top web links.
## Project Structure
```
TELE CHAT BOT/
│
├── bot/                      # Bot Package
│   ├── __init__.py           # Marks 'bot' as a package
│   ├── config.py             # Environment variables & settings
│   ├── database.py           # MongoDB connection and operations
│   ├── gemini.py             # Integration with Google Gemini AI
│   ├── file_handler.py       # Handles document and image processing
│   ├── handlers.py           # Handles user interactions & messages
│   ├── websearch.py         # Implements web search functionality
│
└── main.py                   # Entry point to start the bot
```
## main.py

The `main.py` file serves as the entry point for the Tele Chat Bot. It initializes the bot, sets up command and message handlers, and starts the bot's polling process to listen for incoming messages and commands.

### Key Components:
- **Logging**: Configures logging to capture errors.
- **Bot Initialization**: Uses the Telegram Bot API token to create an application instance.
- **Handlers**: Adds various handlers to manage different types of user interactions:
  - `CommandHandler("start", start)`: Handles the `/start` command to initiate interaction.
  - `CommandHandler("websearch", web_search)`: Handles the `/websearch` command for web searches.
  - `MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)`: Handles text messages.
  - `MessageHandler(filters.CONTACT, save_phone)`: Handles contact sharing.
  - `MessageHandler(filters.Document.ALL, handle_document)`: Handles document uploads.
  - `MessageHandler(filters.PHOTO, handle_photo)`: Handles photo uploads.
- **Bot Execution**: Starts the bot and begins polling for updates.

## config.py

The `config.py` file is responsible for loading and managing environment variables required for the bot's operation. It ensures that all necessary configurations are available and logs any errors encountered during the process.

### Key Components:
- **Logging Configuration**: Sets up logging to capture errors.
- **Environment Variables**: Loads essential environment variables such as `MONGO_URI`, `GEMINI_API_KEY`, and `TELEGRAM_BOT_TOKEN` using `os.environ`.
- **Error Handling**: Logs and raises errors if any required environment variables are missing or if there is an issue loading them.

```python
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
```
## database.py

The `database.py` file manages the connection to the MongoDB database and defines the collections used by the Tele Chat Bot. It ensures that the bot can store and retrieve data efficiently.

### Key Components:
- **Logging Configuration**: Sets up logging to capture errors.
- **Environment Variables**: Loads essential environment variables such as `MONGO_URI`, `MONGO_USERNAME`, `MONGO_PASSWORD`, `MONGO_CLUSTER`, and `MONGO_DB_NAME` using `os.environ`.
- **MongoDB Connection**: Establishes a connection to the MongoDB database using the provided URI.
- **Collections**: Defines the collections for users, chat history, and file metadata.
- **Error Handling**: Logs and raises errors if any required environment variables are missing or if there is an issue connecting to the database.

## websearch.py

The `websearch.py` file implements the functionality for performing web searches based on user queries. It defines an asynchronous function to handle the `/websearch` command.

### Key Components:
- **Logging**: Configures logging to capture errors.
  ```python
  import logging
  logging.basicConfig(level=logging.ERROR)
  logger = logging.getLogger(__name__)
  ```
- **Query Extraction**:
Extracts the search query from the command arguments using context.args.
- **Usage  Prompt**: If no query is provided, it prompts the user with the correct usage of the command.
- **Error handling**:  Catches and logs any exceptions that occur during the execution of the function and notifies the user if the search fails.

The function is intended to be integrated with the Telegram bot's command handling system, allowing users to perform web searches directly from the chat interface.

## gemini.py

The `gemini.py` file integrates the Google Gemini AI for generating text responses based on user prompts. It configures the Gemini API and defines a function to get responses from the AI.

### Key Components:
- **Logging**: Configures logging to capture errors.
  ```python
  import logging
  logging.basicConfig(level=logging.ERROR)
  logger = logging.getLogger(__name__)
  ```
- **Environment Variables**: Retrieves the Gemini API key from environment variables.
    ```python
    import os
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    ```
- **API Configuration**: Sets the API Key for the Gemini client.
    ```python
    import google.generativeai as gemini
    gemini.configure(api_key=gemini_api_key)
    ```
- **Response Generation**: Defines the `get_gemini_response` function to generate text responses using the Gemini API.
    ```python
    def get_gemini_response(prompt):
    response = gemini.generate_text(prompt=prompt)
    return response
    ```
The `gemini.py` file is essential for integrating the Google Gemini AI into the bot, enabling it to generate intelligent text responses based on user inputs.

## handlers.py

The `handlers.py` file manages user interactions and messages for the Telegram bot. It defines several asynchronous functions to handle different types of user inputs and commands.

### Key Components:
- **Logging**: Configures logging to capture errors.
  ```python
  import logging
  logging.basicConfig(level=logging.ERROR)
  logger = logging.getLogger(__name__)

- **Databse Collections**: imports user and chat collections from the database module.
    ```python
    from bot.database import users_collection, chats_collection
    ```
- **Gemini Integration**: imports the function to get responses from the Google Gemini AI.
    ```python
    from bot.gemini import get_gemini_response

## Installation and Setup
1. Clone the Repository
    ```python 
    git clone https://github.com/DarkKnight845/tele-chat-bot.git
    ```
2. Install Dependencies
    ```python
    pip install -r requirements.txt
    ```
3. Set Up Environment Variables
Manually export environment variables or add them to your terminal startup file.
4. Run the Bot
    ```python
    python main.py
    ```
