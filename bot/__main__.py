#!/usr/bin/env python3
# BOT BY @PARVSHAH_01 
# JUST SEND ME A FILE I WILL UPLOAD IT TO CLOUD

import pyrogram
from bot.filetocloud import CloudBot
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    CloudBot().run()

