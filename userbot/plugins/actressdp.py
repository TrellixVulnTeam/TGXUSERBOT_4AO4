#Made By @xhrvan Keep Credits If You Are Goanna Kang This Lol

#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#Usage .actressdp Im Not Responsible For Any Ban caused By This
import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from TGXBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/703416e1df8da896006fa.jpg",
    "https://telegra.ph/file/5015b8f482ee07e33f4ff.jpg",
    "https://telegra.ph/file/92df64c8af7207064bb08.jpg",
    "https://telegra.ph/file/8cf113e7331738315da69.jpg",
    "https://telegra.ph/file/3a873c493ef8f66aca71d.jpg",
    "https://telegra.ph/file/d7e87573d8ab5b1843417.jpg",
    "https://telegra.ph/file/2c62f191601d739331a20.jpg",
    "https://telegra.ph/file/90f4efd903ea9f388f5be.jpg",
    "https://telegra.ph/file/5c2ad9d21711540ea7b41.jpg",
    "https://telegra.ph/file/d7014591bbfcbfad2e739.jpg",
    "https://telegra.ph/file/d074af201129caf87ae9b.jpg",
    "https://telegra.ph/file/7764e1dab57f51fea8cd6.jpg",
    "https://telegra.ph/file/b19801e4180f4088bea43.jpg",
    "https://telegra.ph/file/30ef7d82d2de0e894ee6b.jpg",
    "https://telegra.ph/file/2c6a93458ae5523ae3c72.jpg",
    "https://telegra.ph/file/d75a9f302b959ea4ce847.jpg",
    "https://telegra.ph/file/7f5eeb8fc545dbdd949b5.jpg",
    "https://telegra.ph/file/80b2b329287d6a7f97dec.jpg",
    "https://telegra.ph/file/7a6508814505e68a58d96.jpg",
    "https://telegra.ph/file/3482f74dc78b031be539c.jpg",
    "https://telegra.ph/file/34c4051ff16068035dcac.jpg",
    "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg",
    "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg",
    "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",
    "https://telegra.ph/file/344ca22b35868c0a7661d.jpg",
    "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg",
    "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg",
    "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",
    "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg",
    "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg",
    "https://telegra.ph/file/226f1d1a7971e12352c07.jpg",
    "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",
    "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",
    "https://telegra.ph/file/ebad7b0102044f518031d.jpg",
    "https://telegra.ph/file/7567774412fb76ceba95c.jpg",
    "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",
    "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",
    "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg",
    "https://telegra.ph/file/0d7fcb82603b5db683890.jpg",
    "https://telegra.ph/file/44595caa95717f4db4788.jpg",
    "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg",
    "https://telegra.ph/file/733425275da19cbed0822.jpg",
    "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg",
    "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",
    "https://telegra.ph/file/a38aa50d009835177ac16.jpg",
    "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg",
    "https://telegra.ph/file/96e801400487d0a120715.jpg",
    "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",
    "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",
    "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg",
    "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg",
    "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",
    "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg",
    "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg",
]


@borg.on(admin_cmd(pattern="actressdp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
CmdHelp("actressdp").add_command(
       'actressdp', None, 'Starts autodp of Actress'
).add()
