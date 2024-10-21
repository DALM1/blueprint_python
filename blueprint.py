import os
from PIL import Image, ImageDraw, ImageFont

def create_blueprint(filename, text_elements, shapes, width=800, height=600):
    image = Image.new('RGB', (width, height), color=(25, 100, 150))
    draw = ImageDraw.Draw(image)
    white = (255, 255, 255)

    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=white, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=white, width=1)

    for shape in shapes:
        shape_type = shape['type']
        coords = shape['coords']
        if shape_type == 'rectangle':
            draw.rectangle(coords, outline=white, width=2)
        elif shape_type == 'ellipse':
            draw.ellipse(coords, outline=white, width=2)
        elif shape_type == 'line':
            draw.line(coords, fill=white, width=3)

    try:
        font = ImageFont.truetype("assets/arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()

    for text in text_elements:
        draw.text((text['x'], text['y']), text['content'], font=font, fill=white)

    if not os.path.exists('output'):
        os.makedirs('output')
    image.save(f'output/{filename}')
