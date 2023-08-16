def set_front_run(update, context):
    query = update.callback_query
    query.answer()
    current_markup = query.message.reply_markup

    for row in current_markup.inline_keyboard:
        for button in row:
            if 'callback_front_run' in button.callback_data:
                if button.text == '⛽️Frontrun: 🟢':
                    button.text = '⛽️Frontrun: 🔴'
                    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=button.callback_data.split('-')[1])
                    button.callback_data = "callback_front_run-0"
                else:
                    button.text = '⛽️Frontrun: 🟢'
                    message = "⛽️<i> Frontrun gas is now enabled. Your buys will now frontrun other buys for that token to have your swap be placed first. Transaction is sent at the end of the block, so there may be a small delay before receiving a response. Note that this may result in high gas cost.</i>"
                    res = context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode="HTML")
                    button.callback_data = "callback_front_run-" + str(res.message_id)

    query.edit_message_reply_markup(reply_markup=current_markup)
