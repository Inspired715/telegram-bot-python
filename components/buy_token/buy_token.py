from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def set_buy_tokens_msg(update, context):
    msg = "🛠 <b>Buy Tokens | </b><a href='https://learn.unibot.app/product-guides/multi-wallet-fast-swaps'>Tutorial</a>"
    msg += " -Set your buy settings using the menu below, then enther the token address to buy. Using high slippage may result in fronttun or sandwich attacks.\n"
    msg += "To be protected from MEV attacks, use private transactions.\n"
    msg += "   -<i>Buy Amount:</i> the amt of ETH to spend\n"
    msg += "   -<i>Slippage: </i><a href='https://help.coinbase.com/en/coinbase/trading-and-funding/advanced-trade/slippage'>Definition</a>\n"
    msg += "⬩<b>Gas:</b><code> 28 GWEI </code> ⬩<b>Block:</b><code> 1879118 </code> ⬩<b>ETH:</b><code> $1846 </code>\n"

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('↰ Main Menu', callback_data='callback_main_menu'),
                InlineKeyboardButton('✖ Close', callback_data='callback_close')
            ],
            [
                InlineKeyboardButton('👁‍🗨Private Tx: 🔴', callback_data='callback_private_tx')
            ],
            [
                InlineKeyboardButton('🛡Fail Guard: 🔴', callback_data='callback_fail_guard-0'),
                InlineKeyboardButton('⛽️Frontrun: 🔴', callback_data='callback_front_run-0')
            ],
            [
                InlineKeyboardButton('▓▓▓▓ SELECT WALLETS ▓▓▓▓', callback_data='callback_select_wallets')
            ],
            [
                InlineKeyboardButton('w1 ✅', callback_data='callback_wallet_one'),
                InlineKeyboardButton('w2 ✅', callback_data='callback_wallet_two'),
                InlineKeyboardButton('w3 ✅', callback_data='callback_wallet_thr')
            ],
            [
                InlineKeyboardButton('▓▓▓▓▓ BUY AMOUNT ▓▓▓▓▓', callback_data='callback_buy_amount')
            ],
            [
                InlineKeyboardButton('0.1 ETH ✅', callback_data='callback_eth_1'),
                InlineKeyboardButton('0.3 ETH', callback_data='callback_eth_3'),
                InlineKeyboardButton('0.5 ETH', callback_data='callback_eth_5')
            ],
            [
                InlineKeyboardButton('1.0 ETH', callback_data='callback_eth_10'),
                InlineKeyboardButton('Custom:--', callback_data='callback_custom_over')
            ],
            [
                InlineKeyboardButton('📝 Enter Token Address', callback_data='callback_enter_token-0')
            ]
        ]
    )

    context.bot.send_message(chat_id=update.effective_chat.id, text=msg, reply_markup=markup, parse_mode="HTML", disable_web_page_preview=True, disable_notification=True)