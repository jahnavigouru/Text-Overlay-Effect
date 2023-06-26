import cv2
import numpy as np

# Load the source image
source_image = cv2.imread("source/swami.jpg")

# Load the target image
target_image = cv2.imread("target/p1.png")

# Get the dimensions of the source image
source_height, source_width, _ = source_image.shape

# Get the dimensions of the target image
target_height, target_width, _ = target_image.shape

print(source_height, source_width)
print(target_height, target_width)

# Create a new image with the same dimensions as the target image
new_image = np.zeros((source_height, source_width, 4), dtype=np.uint8)

# Loop through each pixel in the target image
for y in range(source_height):
    for x in range(source_width):

        if np.array_equal(target_image[y, x], [255, 255, 255]):
            # Fill with transparent color (RGBA: 0, 0, 0, 0)
            new_image[y, x] = [0, 0, 0, 0]
            # new_image[y, x] = [255, 255, 255, 255]
        else:
            source_pixel = source_image[y, x]
            new_image[y, x] = np.append(source_pixel, 255)  # Add alpha channel as fully opaque
            if source_image[y, x].tolist() != [255, 255, 255]:
                print(source_image[y,x], new_image[y,x])

# Save the new image
cv2.imwrite("result/chessBoard.png", new_image)
