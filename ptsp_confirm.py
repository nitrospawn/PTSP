import telebot
import gspread
from google.oauth2.credentials import Credentials

# Telegram bot token
TELEGRAM_TOKEN = '6423181297:AAHycTrudw0YoAEK165frKnqKfYT_z1yfHg'

# Google Sheets API setup
SCOPES = ['https://docs.google.com/spreadsheets/d/1ov8u5UPlJ_eB3S_eskhDLh9H4fRWVkbT/edit?usp=sharing&ouid=109711035819875882085&rtpof=true&sd=true']
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
