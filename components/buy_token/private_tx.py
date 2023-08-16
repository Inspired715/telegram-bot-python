from telegram import InlineKeyboardButton

def set_private_tx_on(update):
    query = update.callback_query
    query.answer()
    current_markup = query.message.reply_markup
    private_on = True
    buttons_to_remove = ['callback_enter_token-0']
    for row in current_markup.inline_keyboard:
        for button in row:
            if button.callback_data == 'callback_private_tx':
                if button.text == '👁‍🗨Private Tx: 🟢':
                    button.text = '👁‍🗨Private Tx: 🔴'
                    private_on = False
                else:
                    button.text = '👁‍🗨Private Tx: 🟢'
                    private_on = True
            elif "callback_enter_token" in button.callback_data:
                buttons_to_remove = [button.callback_data]
    if private_on == True:
        current_markup.inline_keyboard = [
            [button for button in row if button.callback_data not in buttons_to_remove]
            for row in current_markup.inline_keyboard
        ]
        additional_buttons = [
            [InlineKeyboardButton("▓▓▓▓▓▓ SLIPPAGE ▓▓▓▓▓▓", callback_data='callback_slippage')],
            [
                InlineKeyboardButton('5%', callback_data='callback_wallet_5_per'),
                InlineKeyboardButton('10% ✅', callback_data='callback_wallet_10_per'),
                InlineKeyboardButton('20%', callback_data='callback_wallet_20_per')
            ],
            [
                InlineKeyboardButton('Custom:--', callback_data='callback_custom_over_private'),
                InlineKeyboardButton('Auto', callback_data='callback_auto')
            ],
            [
                InlineKeyboardButton('📝 Enter Token Address', callback_data='callback_enter_token-0'),
            ]
        ]
        current_markup.inline_keyboard.extend(additional_buttons)
    else:
        buttons_to_remove = ['callback_slippage', 'callback_wallet_5_per', 'callback_wallet_10_per','callback_wallet_20_per','callback_custom_over_private','callback_auto']
        current_markup.inline_keyboard = [
            [button for button in row if button.callback_data not in buttons_to_remove]
            for row in current_markup.inline_keyboard
        ]
        

    query.edit_message_reply_markup(reply_markup=current_markup)