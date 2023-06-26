from PIL import Image

# Open the source image
source_image = Image.open("source/tennis.jpeg")

# Open the target image
target_image = Image.open("target/tennis3pt600.png")

# Get the width and height of the source image
source_width, source_height = source_image.size

print(source_width, source_height)

# Get the width and height of the target image
target_width, target_height = target_image.size

print(target_width, target_height)

# Create a new image with the same size as the target image
new_image = Image.new("RGB", (source_width, source_height))

# Loop through each pixel in the target image
for y in range(source_height):
    for x in range(source_width):
        # Check if the pixel coordinates are within the source image bounds
        if x < source_width and y < source_height:
            print(target_image.getpixel((x, y)))
            if target_image.getpixel((x, y)) == (255, 255, 255) or target_image.getpixel((x, y)) == 255:
                source_pixel = (255, 255, 255)
            else:
                source_pixel = source_image.getpixel((x, y))
        else:
            source_pixel = (255, 255, 255) 

        new_image.putpixel((x, y), source_pixel)

# Save the new image
new_image.save("result/tennis3pt600PIL.png")
