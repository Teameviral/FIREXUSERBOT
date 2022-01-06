import os
import re
import time

from PIL import Image
from telethon.tl.types import MessageEntityPre
from telethon.utils import add_surrogate

# convertions are done here...


def parse_pre(text):
    text = text.strip()
    return (
        text,
        [MessageEntityPre(offset=0, length=len(add_surrogate(text)), language="")],
    )


# make a image
def convert_toimage(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.jpg", "jpeg")
    os.remove(image)
    return "./temp/temp.jpg"


# make a sticker
async def convert_tosticker(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.webp", "webp")
    os.remove(image)
    return "./temp/temp.webp"


# deal with it...
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


StartTime = time.time()

# FIREX
