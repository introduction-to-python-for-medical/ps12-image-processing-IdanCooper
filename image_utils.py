from PIL import Image
import numpy as np
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


