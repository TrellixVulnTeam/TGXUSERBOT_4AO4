
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from userbot import ALIVE_NAME, CMD_HELP
from TGXBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import version, events
from math import ceil
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

PM_IMG = "https://telegra.ph/file/9579285e28a6031374b62.jpg"
pm_caption ="**🔱LegendBøt IS Awake🔱**\n\n"
pm_caption += f"**🇮🇳 Telethon : TELETHON-1.19.0**\n"
pm_caption += f"**🇮🇳 Python : PYTHON-3.8.5**\n"
pm_caption += f"**🇮🇳 I'll Be With You Master Till My Dyno Ends!!☠**\n"
pm_caption += f"**🇮🇳 OWNER` : @xhrvan**\n"
pm_caption += f"**🇮🇳 MY BOSS😊: {DEFAULTUSER}**\n"
pm_caption += f"**🇮🇳 GROUP : [TGX](https://t.me/https://t.me/TGxBOTz_CHAT)**\n" 
pm_caption += " [✨REPO✨](https://github.com/xhrvan/TGXBOTZ) 🔹 [📜License📜](https://github.com/LEGEND-OS/TGXBOT/blob/master/LICENSE)" 
@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(alive):
   if alive.fwd_from:
      return
   await alive.get_chat()
   await alive.delete()
   """ For .alive command, check if the bot is running. """
   await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
   await alive.delete()
                
           
    
    
CmdHelp("αωακє").add_command(
  'awake', None, 'Awake Or Not'
).add()
