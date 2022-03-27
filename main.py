import telebot
import config
from telegram import Bot
from telegram.ext import Updater,CommandHandler
updater = Updater(config.TOKEN)

#banner
#def
print("The bot is running..")
def start_bot(updata,context):
    updata.message.reply_text("Welcome to lord4tb bot")
    print("[ * ] Send start ")
def error(updata,context):
    print(f"Updata {updata} error {context.error}")

#handlers
updater.dispatcher.add_handler(CommandHandler("start",start_bot))
updater.dispatcher.add_error_handler(error)
updater.start_polling()
