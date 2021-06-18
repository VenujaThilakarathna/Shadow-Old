from telegram import InlineKeyboardButton, InlineKeyboardMarkup

HELP_BUTTONS = [[InlineKeyboardButton(text="🔙Back", callback_data="help_back")]]

__help__ = """
 ✪ /tr or /tl: To translate to your language, by default language is set to english, use /tr <lang code> for some other language!
 ✪ /splcheck: As a reply to get grammar corrected text of gibberish message.
"""
__mod_name__ = "Translator 🔄"
