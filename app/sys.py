import requests
from PIL import Image, ImageDraw, ImageFont

"""

test à faire pour les textes : H -> 1.2 ou 1.5 ou < 2

"""


def _font_selector(name: str, size: int):
    return ImageFont.truetype('font/%s.ttf' % name, size=size)


def addText(self, size: list, text: list, color: tuple, font_name: list):
    for s, t, fn in zip(size, text, font_name):
        self.text(s, t, color, _font_selector(fn[0], fn[1]))


def create_image(username, color):
    width, height = 480, 300
    img = Image.new('RGB', (width, height), color=(55, 55, 55))

    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(username, font=_font_selector("MouseMemoirs-Regular", 44))

    # Draw text and middle line

    draw.text(((width - w) / 2, 10), username, fill=(242, 248, 255), font=_font_selector("MouseMemoirs-Regular", 44))

    draw.line((width / 2, 80, width / 2, 250), fill=(73, 73, 73), width=1)  # POS : (x, l, x, l!=)

    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    # print(data)
    try:
        addText(draw, [
            ((width - w) / 5, 110),
            ((width - w) / 5, (height - h) / 1.8),
            ((width - w) / 5, (height - h) / 1.8 + 32.5)],
                [
                    f"{recover_data(username, 'language')[0][0]}: {recover_data(username, 'language')[0][1]}%",
                    f"{recover_data(username, 'language')[1][0]}: {recover_data(username, 'language')[1][1]}%",
                    f"{recover_data(username, 'language')[2][0]}: {recover_data(username, 'language')[2][1]}%"
                ], (242, 248, 255),
                [("MouseMemoirs-Regular", 30), ("MouseMemoirs-Regular", 25), ("MouseMemoirs-Regular", 20)])
    except IndexError:
        pass
    print((height - h) / 1.8)
    try:
        addText(draw, [
            ((width - w) / 1.1, 110),
            ((width - w) / 1.1, (height - h) / 1.8),
            ((width - w) / 1.1, (height - h) / 1.8 + 32.5)],
                [
                    f"1. {recover_data(username, 'repos')[0]}",
                    f"2. {recover_data(username, 'repos')[1]}",
                    f"3. {recover_data(username, 'repos')[2]}"
                ], (242, 248, 255),
                [("MouseMemoirs-Regular", 30), ("MouseMemoirs-Regular", 25), ("MouseMemoirs-Regular", 20)])
    except IndexError:
        pass

    if data['blog'] not in [None, 'null', 'Null', '']:
        print(data['blog'])
        draw.text((10, 270), data['blog'], fill=(242, 248, 255), font=_font_selector("MouseMemoirs-Regular", 20))
    else:
        print("Il n'y a pas de blog")

    img.convert('RGB').save(f'app/image/{username}.png')


def sumWithPerfection(num, n):
    integer = int(num * (10 ** n)) / (10 ** n)
    if float(integer) != 0.0:
        return float(integer)


def recover_data(username, step):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    data = response.json()

    name_of_repo = [element["name"] for element in data if element["name"]]
    duplicated = {element["language"] for element in data if element["language"]}  # Je récupère et stock les doublons
    all_langs = [data[element]["language"] for element in range(len(data)) if
                 data[element]["language"] in duplicated]  # Je récupère et stock tout les languages
    total = [all_langs.count(k) for k in duplicated]  # Je récupère le nombre de fois que le language apparait
    numbers = {obj: sumWithPerfection(100 * all_langs.count(obj) / sum(total), 1) for obj in
               duplicated}  # Je fais mes statistique pour chaque language

    sorted_dict = sorted(numbers.items(), key=lambda x: x[1], reverse=True)

    items = []

    if step == 'repos':
        for i in range(len(name_of_repo)):
            items.append(name_of_repo[i])
            i += 1
    elif step == 'language':
        for k, item in enumerate(dict(sorted_dict).items()):
            if k < 3:
                items.append(item)

    return items
