from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6051829115:AAEwIwAdNrpOAbb18F1t1D2wcJ3I3K-4x1Q").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()