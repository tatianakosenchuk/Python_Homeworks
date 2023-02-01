from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logger
from config import TOKEN
from bot_menu import *




app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sum",sum_bot))
app.add_handler(CommandHandler("sub", sub_bot))
app.add_handler(CommandHandler("mult", mult_bot))
app.add_handler(CommandHandler("div", div_bot))
app.add_handler(CommandHandler("pow", pow_bot))
app.add_handler(CommandHandler("sqrt", sqrt_bot))
print('bot started')
app.run_polling()