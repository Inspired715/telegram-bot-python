import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from components.main import set_main_menu
from components.close import set_close_window
from components.buy_token.buy_token import set_buy_tokens_msg
from components.buy_token.private_tx import set_private_tx_on
from components.buy_token.fail_guard import set_fail_guard
from components.buy_token.front_run import set_front_run
from components.buy_token.enter_token import set_enter_token
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')

def callback_event(update, context):
    try:
        key = update.callback_query.data

        if key == "callback_buy_tokens":
            set_buy_tokens_msg(update, context)
        elif key == "callback_main_menu":
            set_main_menu(update, context)
        elif "callback_fail_guard" in key:
            set_fail_guard(update, context)
        elif "callback_front_run" in key:
            set_front_run(update, context)
        elif "callback_enter_token" in key:
            set_enter_token(update, context)
        elif key == "callback_close":
            set_close_window(update)
        elif key == "callback_private_tx":
            set_private_tx_on(update)
    except Exception as e:
        print(e)

def main():
    try:
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('start', set_main_menu))
        dispatcher.add_handler(CallbackQueryHandler(callback_event))

        print('Starting...')
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()