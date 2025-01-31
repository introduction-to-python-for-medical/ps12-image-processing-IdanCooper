

from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def load_image(path):
    i = Image.open(path)
    return np.array(i)

def edge_detection(image):
    
    
    grey = np.mean(image, axis=2)
    grey = np.pad(grey,pad_width =((1,1),(1,1)) ,constant_values=0)
    y_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    x_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edgeX = convolve2d(grey, x_filter)[1:-1,1:-1]
    edgeY = convolve2d(grey, y_filter)[1:-1,1:-1]
    edgeMAG = (edgeX**2 + edgeY**2)**0.5
    return edgeMAG


image = load_image('shoobydooby.jpg')
clean_image = median(image, ball(3))
binary_image = edge_detection(clean_image) <20
plt.imshow(binary_image, cmap='gray')
plt.imsave("binary_image.png", binary_image, cmap='gray')
