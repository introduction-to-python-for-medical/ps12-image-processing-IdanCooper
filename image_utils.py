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
    
 
    image = np.mean(image, axis=2)
    image = np.pad(image,pad_width =((1,1),(1,1)) ,constant_values=0)
    y_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    x_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edgeX = convolve2d(image, x_filter, mode="same", boundary="fill", fillvalue=0)
    edgeY = convolve2d(image, y_filter, mode="same", boundary="fill", fillvalue=0)
    edgeMAG = (edgeX**2 + edgeY**2)**0.5
    return edgeMAG
