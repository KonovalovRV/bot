from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()  # /sum  123  123
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')


def leap_year(a):
    if a % 4 == 0 and a % 100 != 0:
        return int(366)
    if a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
        return int(366)
    else:
        return int(365)


# Количество дней до нового года - необходимо ввести любой год, например 2029. 
async def hy_quantity_days_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    year = msg.split()
    future_year = int(year[1])
    count = - int(datetime.datetime.now().strftime('%j'))
    current_year = int(datetime.datetime.now().strftime('%Y'))
    while future_year > current_year:
        count += leap_year(future_year)
        future_year -= 1
    await update.message.reply_text(f'До нового {year[1]} года осталось {count} дней')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/sum\n/hy\n/help')
