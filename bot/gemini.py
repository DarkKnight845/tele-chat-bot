import os
import logging
import google.generativeai as gemini

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Get the Gemini key from environment variables
    gemini_api_key = os.environ["GEMINI_API_KEY"]

    # Set the API key for Gemini
    gemini.configure(api_key=gemini_api_key)

    def get_gemini_response(prompt):
        response = gemini.generate_text(prompt=prompt)
        return response
    print("Gemini is configured succesfully")

except KeyError as e:
    logger.error(f"❌ Missing environment variable: {e}")
    raise ValueError(f"Missing required environment variable: {e}")

except Exception as e:
    logger.error(f"❌ Error configuring Gemini: {e}")
    raise