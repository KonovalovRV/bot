
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'hi {update.effective_user.first_name}')


app = ApplicationBuilder().token("6051829115:AAEwIwAdNrpOAbb18F1t1D2wcJ3I3K-4x1Q").build()
print("server start")
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.run_polling()
