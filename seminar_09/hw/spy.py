import datetime

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    file = open('db_logs.csv', 'a')
    file.write(f'{datetime.datetime.now()},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()