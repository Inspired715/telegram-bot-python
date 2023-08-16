from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from db import inset_wallet_info, get_wallet_address

def generate_eth_address(update):
    private_key = keccak_256(token_bytes(32)).digest()
    publick_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(publick_key).digest()[-20:]
    private_key = private_key.hex()
    eth_addr = '0x' + addr.hex()
    
    inset_wallet_info(update.message.chat.first_name, update.message.chat.last_name, update.message.chat.username, update.message.chat.id, eth_addr, private_key)
    
    return eth_addr

def set_main_menu(update, context):
    res = get_wallet_address(update.message.chat.id)
    w1 = ""
    w2 = ""
    w3 = ""
    if not res:
        w1 = generate_eth_address(update)
        w2 = generate_eth_address(update)
        w3 = generate_eth_address(update)
    else:
        
        if len(res) != 3:
            print('Data is corrupted')
            return "500"
        w1 = res[0]
        w2 = res[1]
        w3 = res[2]

    message = "Welcome to Unibot. You are now registered and have been assigned new wallets.\n"
    message += "Fund the wallets provide to start swapping and sniping.\n"
    message += "⬩<b>Gas:</b><code> 28 GWEI </code> ⬩<b>Block:</b><code> 1879118 </code> ⬩<b>ETH:</b><code> $1846 </code>\n"
    message += "\n"
    message += "🦄 <b>Unibot ⬩ Elite Dex Sniper ⬩ </b><a href='https://unibot.app'><b> Website </b></a> 🦄\n"
    message += "Snipe & swapat elite speeds for free. Uniswap v2 and v3 are supported.\n"
    message += "\n"
    message += "═══ Your Wallets ═══\n"
    #Wallet w1
    message += "▰ <a href='https://etherscan.io/address/"+ w1 +"'>Wallet⬩w1</a>\n"
    message += "<b>Balance:</b>\n"
    message += "<pre>0.0 ETH</pre>\n"
    message += "⬩\n"
    message += "<pre>$0</pre>\n"
    message += "<b>Transactions:</b>\n"
    message += "<pre>0</pre>\n"
    message += "<b>Address:</b><code>"+ w1 +"</code>\n"
    message += "\n"
    #Wallet w2
    message += "▰ <a href='https://etherscan.io/address/"+ w2 +"'>Wallet⬩w2</a>\n"
    message += "<b>Balance:</b>\n"
    message += "<pre>0.0 ETH</pre>\n"
    message += "⬩\n"
    message += "<pre>$0</pre>\n"
    message += "<b>Transactions:</b>\n"
    message += "<pre>0</pre>\n"
    message += "<b>Address:</b><code>"+ w2 +"</code>\n"
    message += "\n"
    #Wallet w3
    message += "▰ <a href='https://etherscan.io/address/"+ w3 +"'>Wallet⬩w3</a>\n"
    message += "<b>Balance:</b>\n"
    message += "<pre>0.0 ETH</pre>\n"
    message += "⬩\n"
    message += "<pre>$0</pre>\n"
    message += "<b>Transactions:</b>\n"
    message += "<pre>0</pre>\n"
    message += "<b>Address:</b><code>"+ w3 +"</code>\n"
    message += "\n"

    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Buy Tokens', callback_data='callback_buy_tokens'),
                InlineKeyboardButton('Sell Tokens', callback_data='callback_sell_tokens')
            ],
            [
                InlineKeyboardButton('Buy Limit', callback_data='callback_buy_limit'),
                InlineKeyboardButton('Sell Limit', callback_data='callback_sell_limit')
            ],
            [
                InlineKeyboardButton('Mirror Sniper', callback_data='callback_mirror_sniper'),
                InlineKeyboardButton('Method Sniper', callback_data='callback_method_sniper')
            ],
            [
                InlineKeyboardButton('Token Balances', callback_data='callback_token_balance'),
                InlineKeyboardButton('PNL Analysis', callback_data='callback_pnl_analysis'),
                InlineKeyboardButton('Settings', callback_data='callback_settings')
            ]
        ]
    )

    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=markup, parse_mode="HTML", disable_web_page_preview=True, disable_notification=True)
