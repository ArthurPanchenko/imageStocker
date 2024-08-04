import textwrap
import random

from PIL import Image, ImageDraw, ImageFont


BACKGROUNDS = [
    'back1.jpg',
    'back2.jpg',
    'back3.jpg'
]

CHARACTERS = [
    'char1.png',
    'char2.png',
    'char3.png'
]


async def generate_image(text):

    background_path = 'services/templates/backgrounds/' + random.choice(BACKGROUNDS)
    character_path = 'services/templates/characters/' + random.choice(CHARACTERS)

    picture = Image.open(background_path)
    character = Image.open(character_path).resize((500, 650))


    picture.paste(character, (1300, 350), mask=character)
    
    lines = textwrap.wrap(text, width=12)
    draw = ImageDraw.Draw(picture)
    font = ImageFont.truetype('services/templates/Queensides.ttf', 120)
    y = 150

    for line in lines:
        draw.text((150, y), line, (255, 255, 255), font=font)
        y += 130
    
    path_to_image = f'services/media/{random.randint(0, 999)}.png'

    picture.save(path_to_image)
    
    return path_to_image


