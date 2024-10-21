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

def get_text_input():
    texts = []
    while True:
        add_text = input("Do you want to add text? (yes/no): ").lower()
        if add_text == 'no':
            break
        content = input("Enter the text: ")
        x = int(input("Enter the x position for the text: "))
        y = int(input("Enter the y position for the text: "))
        texts.append({'content': content, 'x': x, 'y': y})
    return texts

def get_shapes_input():
    shapes = []
    while True:
        add_shape = input("Do you want to add a shape? (yes/no): ").lower()
        if add_shape == 'no':
            break
        shape_type = input("Enter the shape type (rectangle, ellipse, line): ").lower()
        x1 = int(input("Enter the x1 coordinate: "))
        y1 = int(input("Enter the y1 coordinate: "))
        x2 = int(input("Enter the x2 coordinate: "))
        y2 = int(input("Enter the y2 coordinate: "))
        shapes.append({'type': shape_type, 'coords': [(x1, y1), (x2, y2)]})
    return shapes

def main():
    filename = input("Enter the filename for the blueprint (without extension): ") + ".png"
    texts = get_text_input()
    shapes = get_shapes_input()
    create_blueprint(filename, texts, shapes)
    print(f"Blueprint saved as {filename} in the output folder.")

if __name__ == "__main__":
    main()
