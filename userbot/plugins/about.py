
import asyncio
import random
from telethon import events
from TGXBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

# Thanks to LEGEND BRO.. 
# animation Idea by @Legend_Mr_Hacker (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/2d41a6b1b3713579c63c2.jpg"
file2="https://telegra.ph/file/9fb5502699714b8eabca3.jpg"
file3="https://telegra.ph/file/f04dcb487d52b97c36a54.jpg"
file4="https://telegra.ph/file/bac71ea81bebea8332f86.jpg"
file5="https://telegra.ph/file/56330a785e4f2a5919e1c.jpg"""" =======================CONSTANTS====================== """
pm_caption = "🔥𝕷êgëñd𝕭øt ιѕ ορ🔥\n\n"
pm_caption += "💌💌 **𝐆𝐨𝐝,𝒚𝒐𝒖 𝒂𝒓𝒆 𝒂𝒍𝒎𝒊𝒈𝒉𝒕𝒚 , 𝗉𝗅𝗌 𝗍𝖺𝗄𝖾 𝖼𝖺𝗋𝖾 𝗈𝖿 𝗆𝗒 𝖻𝖾𝗌𝗍𝗂𝖾 .. 𝗆𝗂𝗌𝗌𝗂𝗇𝗀 𝗁𝗂𝗆 𝗏𝖾𝗋𝗒 𝗆𝗎𝖼𝗁💫😇.**💌💌\n\n"
pm_caption += "༆༄🎀🌹𝕬𝖇𝖔𝖚𝖙 𝕸𝖊 \n\n"
pm_caption += "💫💫**𝕷êgëñd𝕭øt**💫💫 >>》 15.0.0\n"
pm_caption += "😇😇**𝕷êgëñd**😇😇   >>》 [οωиєя](https://t.me/Legend_Mr_Hacker)\n"
pm_caption += f"🔰🔰**𝕸𝖆𝖙𝖊𝖗**🔰🔰  >>》 {DEFAULTUSER}\n"
pm_caption += "❣❣ **𝕷êgëñd𝕭øt**❣❣ >>》 [𝕲𝖗ουρ](https://t.me/Tgxbotz_chat)\n\n"
pm_caption += "🎊🎊 **𝕽𝖊𝖕ο**🎊🎊  >>》 [𝕽єρο](https://github.com/LEGEND-OS/TGXBOT)\n\n"
pm_caption += "[....▄███▄███▄\n....█████████\n.......▀██❣🌹💫😇💫🌹❣███▀\n...............▀█▀\n](https://t.me/Legend_Mr_Hacker)\n\n"
@borg.on(admin_cmd(pattern=r"abot"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    CmdHelp("αϐοτ").add_command(
      'abot', None , 'BEST alive command'
).add()
