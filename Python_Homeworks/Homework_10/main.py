import logging
from telegram.ext import Updater, MessageHandler, filters, CommandHandler, ConversationHandler, CallbackQueryHandler, JobQueue,ApplicationBuilder
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from game import *
from config import TOKEN


async def start(update,_):
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    'Приветствую Вас в игре "Крестики-нолики".\n')
    await update.message.reply_text('Для начала игры введите команду: /start_game\n' 
                                    'Для окончания игры введите команду: /stop')

async def stop(update,_):
    return ApplicationBuilder().END

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                         level=logging.INFO,
#                         filename='bot.log')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))

conv_handler = ConversationHandler(
entry_points=[CommandHandler("start_game", start_game)],

states={
            "CHOOSING_X": [CallbackQueryHandler(cross)],
            "CHOOSING_O": [CallbackQueryHandler(zero)],
        },

fallbacks=[CommandHandler('stop', stop)])
    

app.add_handler(conv_handler)

print('start')
    # Start the Bot
app.run_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

