import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from tracker import get_prices

telegram_bot_token = "YOUR API KEY"
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to Crypto Updates Tracker\n\n''Type /cryptoupdates to Get Crypto Currency Updates \n\n''To get help or to know more about it type /help')

def help(update, context):
    update.message.reply_text('Here are the Commands You can use\n\n''/start --- Start Over\n\n''/cryptoupdates --- Get Crypto Currency Updates\n\n' '/help --- Get Help\n\n' '/contact --- Contact')
   
def contact(update, context):
    update.message.reply_text('Contact Our Developers for any Issue\n\n'' @rahulroy6918 \t @Masken_Madchen \n''Rahul Roy - https://t.me/rahulroy6918\n''Tithi Mukherjee - https://t.me/Masken_Madchen' )                           
                              
def cryptoupdates(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        open_day = crypto_data[i]["open_day"]
        high_day = crypto_data[i]["high_day"]
        low_day = crypto_data[i]["low_day"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\nOpen Day: ${open_day:,.2f}\nHigh 24 Hour: ${high_day:,.2f}\nLow 24 Hour: ${low_day:,.2f}\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("cryptoupdates", cryptoupdates))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("contact", contact))
updater.start_polling()
