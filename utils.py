from skimage.io import imread, imsave
import matplotlib.pyplot as plt

def read_image(path, is_gray=False):
    image = imread(path, as_gray=is_gray)
    return image

def save_image(image, path):
    imsave(path, image)

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()