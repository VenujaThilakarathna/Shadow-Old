from telegram import InlineKeyboardButton, InlineKeyboardMarkup

HELP_BUTTONS = [[InlineKeyboardButton(text="🔙Back", callback_data="help_back")]]

__help__ = """
 ✪/getqr `<reply to image>`: Read QR code
 ✪/makeqr `<text>`: Make QR code from the given message (text, link, etc...)
 """
__mod_name__ = "Qrcode#️⃣"
 
 
