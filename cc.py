import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import imageio.v2 as imageio  # Import imageio.v2 to suppress deprecation warning

# Load the image in grayscale mode ('F' for floating point representation)
image = imageio.imread('Porsche-911-Turbo-S-Exclusive-Series-4k-Wallpaper.jpg', mode='F')

# Define a 3x3 edge detection kernel
kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

# Perform the 2D convolution operation
convolved_image = convolve2d(image, kernel, mode='valid')

# Display the original and convolved images
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(convolved_image, cmap='gray'), plt.title('Convolved Image')
plt.show()
