
# pata nhi sir 👀👀👀👀
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from smartbot import bot as danish_00
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from TGXBOT.utils import admin_cmd, edit_or_reply, sudo_cmd as admin_cmd
from smartbot.cmdhelp import CmdHelp
@bot.on(admin_cmd(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Searching ur bin 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()

@bot.on(admin_cmd(pattern="vbv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@bot.on(admin_cmd(pattern="key ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
  
@bot.on(admin_cmd(pattern="iban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/iban {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
CmdHelp("bin").add_command(
    'bin', None, '.bin <ID>@'
).add_command(
    'iban', None, 'Use And See'
).add_command(
    'key', None, 'Use And See'
).add_command(
    'vbv', None, 'Use And See'
).add()
