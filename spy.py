from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import csv


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'x')
    file.write(
        f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()