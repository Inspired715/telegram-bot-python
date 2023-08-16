def set_fail_guard(update, context):
    query = update.callback_query
    query.answer()
    current_markup = query.message.reply_markup

    for row in current_markup.inline_keyboard:
        for button in row:
            if 'callback_fail_guard' in button.callback_data:
                if button.text == '🛡Fail Guard: 🟢':
                    button.text = '🛡Fail Guard: 🔴'
                    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=button.callback_data.split('-')[1])
                    button.callback_data = "callback_fail_guard-0"
                else:
                    button.text = '🛡Fail Guard: 🟢'
                    message = "🛡<i> Fail guard is now enabled. Unibot will check to see if the transaction will fail before sending</i>"
                    res = context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode="HTML")
                    button.callback_data = "callback_fail_guard-" + str(res.message_id)

    query.edit_message_reply_markup(reply_markup=current_markup)
