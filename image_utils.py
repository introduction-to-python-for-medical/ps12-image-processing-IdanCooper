from PIL import Image
import numpy as np
from scipy.signal import convolve2d



def load_image(path):
    i = Image.open(path)
    return np.array(i)


def edge_detection(image):
    
 
    image = np.mean(image, axis=2)
    y_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    x_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edgeX = convolve2d(image, x_filter, mode="same", boundary="fill")
    edgeY = convolve2d(image, y_filter, mode="same", boundary="fill")
    edgeMAG = (edgeX**2 + edgeY**2)**0.5
  
    return edgeMAG
