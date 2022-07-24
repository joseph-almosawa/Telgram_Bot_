import Responses
import API_KEY
from telegram.ext import *


print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type somthing random to get started!')



def help_command(update, context):
    update.message.reply_text("If you want help! you need to google it first😅 because I need to learn a lot.")

def handel_message(update, context):
    text = str(update.message.text).lower()   # this recives a text from the user 
    response = Responses.replay(text)     # processes it 

    update.message.reply_text(response) #this put it back out to the user


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY.API_KEY, use_context = True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command)) 

    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handel_message))

    dp.add_error_handler(error)
    updater.start_polling(2) # here to put the amount of sec to reply
    updater.idle() #this just to make sure that it continusly stays active 



main()







