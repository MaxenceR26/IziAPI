import requests
from PIL import Image, ImageDraw, ImageFont


def _font_selector(name: str, size: int):
    font = ImageFont.truetype('font/%s.ttf' % name, size=size)
    return font


def create_image(username, color):
    width, height = 480, 300
    img = Image.new('RGB', (width, height), color=(55, 55, 55))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(username, font=_font_selector("MouseMemoirs-Regular", 44))

    # Draw text and middle line

    draw.text(((width - w) / 2, 10), username, fill=(242, 248, 255), font=_font_selector("MouseMemoirs-Regular", 44))

    draw.line((width / 2, 80, width / 2, 250), fill=(255, 255, 255), width=2)  # POS : (x, l, x, l!=)

    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    # print(data)

    if data['blog'] not in [None, 'null', 'Null', '']:
        print(data['blog'])
        draw.text((10, 270), data['blog'], fill=(242, 248, 255), font=_font_selector("MouseMemoirs-Regular", 20))
    else:
        print("Il n'y a pas de blog")

    img.convert('RGB').save(f'app/image/{username}.png')
