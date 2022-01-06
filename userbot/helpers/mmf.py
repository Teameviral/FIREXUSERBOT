import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from userbot.Config import Config


async def draw_to_Text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if "," in text:
        upper_text, lower_text = text.split(",")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, "webp")
    return webp_file


async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(
        "userbot/helpers/styles/No4.ttf", int((70 / 640) * i_width)
    )
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad

    image_name = "eviral.webp"
    img.save(image_name, "WebP")
    return image_name


async def draw_meme(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(
        "userbot/helpers/styles/impact.ttf", int((70 / 640) * i_width)
    )
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad

    lumd = "eviral.png"
    img.save(lumd, "png")
    return lumd
