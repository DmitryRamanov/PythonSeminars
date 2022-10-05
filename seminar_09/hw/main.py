from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import hi_command, menu_command, help_command, getrecords_command, menu1_command, menu2_command
from bot_commands import menu3_command, menu4_command, menu5_command
from controller import tg_start


updater = Updater('5623533832:AAEUg5l49RsSZLFXfT55Ifwe2AYCz_BB23s')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('menu', menu_command))
updater.dispatcher.add_handler(CommandHandler('menu1', menu1_command))
updater.dispatcher.add_handler(CommandHandler('menu2', menu2_command))
updater.dispatcher.add_handler(CommandHandler('menu3', menu3_command))
updater.dispatcher.add_handler(CommandHandler('menu4', menu4_command))
updater.dispatcher.add_handler(CommandHandler('menu5', menu5_command))
updater.dispatcher.add_handler(CommandHandler('getdata', getrecords_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

tg_start()  #считывает БД из файла
print('server start')
updater.start_polling()
updater.idle()