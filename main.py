

from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

from image_utils.py import load_image , edge_detection

image = load_image('shoobydooby.jpg')
clean_image = median(image, ball(3))
edge_detected_image = edge_detection(clean_image)
plt.imsave("edge_detected_image", edge_detected_image, cmap='gray')
