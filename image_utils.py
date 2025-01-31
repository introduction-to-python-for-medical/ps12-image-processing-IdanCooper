from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


def load_image(path):
    image = Image.open(path)
    if image.mode == 'RGB':  
        image = np.mean(image, axis=2)
    final_image = np.array(image)
    return final_image

def edge_detection(image):
    image = np.pad(image,pad_width =((1,1),(1,1)) ,constant_values=0)
    y_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    x_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edgeX = convolve2d(image, x_filter)
    edgeY = convolve2d(image, y_filter)
    edgeX = edgeX[2:-2,2:-2]
    edgeY = edgeY[2:-2,2:-2]

    edgeMAG = (edgeX**2 + edgeY**2)**0.5
    return edgeMAG
