#(Ā©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ā šš«ššš­šØš« : <a href='tg://user?id={OWNER_ID}'>ššš©š©š²šš¢ššš</a>\nā ššš§š š®šš š : <code>šš²š­š”šØš§š</code>\nā šš¢šš«šš«š² : <a href='https://docs.pyrogram.org/'>šš²š«šØš š«šš¦ šš¬š²š§šš¢šØ {__version__}</a>\nā ššØš®š«šš ššØšš : <a href='https://linktr.ee/sk_source_code'>šš„š¢šš¤ š”šš«š</a>\nā šš”šš§š§šš„ : @HappyKidBGMZ\nā šš®š©š©šØš«š­ : @BGM_LinkzZ</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("āŖļø šš„šØš¬š ā©ļø", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
