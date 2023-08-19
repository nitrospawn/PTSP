import telebot
import gspread
from google.oauth2.credentials import Credentials

# Telegram bot token
TELEGRAM_TOKEN = 'vfvvvvv'

# Google Sheets API setup
SCOPES = ['spread sheet url']
creds = None  # Set up credentials

# Initialize Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I can help you search for content in a Google Sheet.")

@bot.message_handler(func=lambda message: True)
def search_google_sheet(message):
    query = message.text.lower()
    # Authenticate with Google Sheets API using creds

    # Search for content in Google Sheet
    # Implement code to search for content in the Google Sheet and check if the content is found

    if content_found:
        bot.reply_to(message, "itex is ptsp")
    else:
        bot.reply_to(message, "Content not found.")

bot.polling()
