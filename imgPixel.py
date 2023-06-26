from PIL import Image

# Open the image
image = Image.open("target/chessBoard.png")

# Get the width and height of the image
width, height = image.size

# Loop through each pixel in the image
pixels = []
for y in range(height):
    for x in range(width):
        # Get the pixel value at (x, y)
        pixel = image.getpixel((x, y))
        if pixel != (255, 255, 255):
            print(x, y, " ", pixel)
        pixels.append(pixel)
