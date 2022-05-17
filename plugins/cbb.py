#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href='tg://user?id={OWNER_ID}'>𝐓𝐡𝐢𝐬 𝐏𝐞𝐫𝐬𝐨𝐧</a>\n○ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <code>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</code>\n○ 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://docs.pyrogram.org/'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐚𝐬𝐲𝐧𝐜𝐢𝐨 {__version__}</a>\n○ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 : <a href='https://linktr.ee/sk_source_code'>𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞</a>\n○ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @HappyKidBGMZ\n○ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 : @BGM_LinkzZ</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("↪️ 𝐂𝐥𝐨𝐬𝐞 ↩️", callback_data = "close")
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
