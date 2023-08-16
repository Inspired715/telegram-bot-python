def set_enter_token(update, context):
    query = update.callback_query
    query.answer()
    current_markup = query.message.reply_markup
    message = "📝 Enter Token Address:"

    for row in current_markup.inline_keyboard:
        for button in row:
            if 'callback_enter_token' in button.callback_data:
                message_id = button.callback_data.split('-')[1]
                if message_id != '0':
                    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_id)
    
    res = context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode="HTML")
    button.callback_data = "callback_enter_token-" + str(res.message_id)
    
    query.edit_message_reply_markup(reply_markup=current_markup)