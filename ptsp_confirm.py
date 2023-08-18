import telebot
import requests
import openpyxl
from io import BytesIO

# Telegram bot token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# GitHub raw file URL
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/username/repository/main/file.xlsx'

# Initialize Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I can help you search for content in an Excel file.")

@bot.message_handler(func=lambda message: True)
def search_excel_content(message):
    query = message.text.lower()

    try:
        excel_content = extract_excel_content(GITHUB_RAW_URL)
        if query in excel_content:
            bot.reply_to(message, "itex is ptsp")
        else:
            bot.reply_to(message, "Content not found.")
    except Exception as e:
        bot.reply_to(message, "An error occurred while processing the file.")

def extract_excel_content(file_url):
    response = requests.get(file_url)
    response.raise_for_status()
    excel_file = BytesIO(response.content)

    wb = openpyxl.load_workbook(excel_file, data_only=True)
    sheet = wb.active

    content = ""
    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            content += str(cell).lower() + " "
    return content

bot.polling()
