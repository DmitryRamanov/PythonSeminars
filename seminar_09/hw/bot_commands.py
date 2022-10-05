from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from controller import tg_show_menu, tg_print_records, tg_search_records
from spy import log

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.full_name}')

def help_command(update: Update, context: CallbackContext):
    # msg = update.message.text # команда пользователя из бота
    # print(msg)
    # update.message.reply_text(f'{msg}')
    log(update, context)
    update.message.reply_text(f'/hi\n/menu\n/menu1\n...\n/menu5\n/getdata\n/help')

def menu_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_show_menu())

def menu1_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_search_records())

def menu2_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_show_menu())

def menu3_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_show_menu())

def menu4_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_show_menu())

def menu5_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_show_menu())

def getrecords_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(tg_print_records())