import numpy as np
import pandas as pd
import matplotlib.image as img
import cv2
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten
from sklearn.cluster import KMeans



def resize(self, show = False):
    # read the image file
    image = img.imread(self)
    w, h = image.shape[:2]

    # resize the image to width = 500
    # then portionally resize the height
    rs_w = 500
    rs_image = cv2.resize(image, (int(rs_w*float(h)/w), rs_w))

    if show:
        # show original image and resized image
        print('New shape :', rs_image.shape)

        plt.figure(figsize=(16,10))
        plt.axis("off")

        plt.subplot(121)
        plt.title('Original image')
        plt.imshow(image)

        plt.subplot(122)
        plt.title('Image after resized')
        plt.imshow(rs_image)
        plt.show()
        
    return rs_image
    

def pixelize(rs_image):
    # create empty list for each color elements: red, green, blue
    r,g,b=[],[],[]

    # iterate through each pixel, store their rgb values in each color lists
    for pixel in rs_image:
        for r_val, g_val, b_val in pixel:
            r.append(r_val)
            g.append(g_val)
            b.append(b_val)

    # normalize rgb values in lists
    nor_red = whiten(r)
    nor_blue = whiten(b)
    nor_green = whiten(g)

    # dataframe of colors
    df = pd.DataFrame({'red':r,'blue':b,'green':g,'scaled_red':nor_red,'scaled_blue':nor_blue,
                    'scaled_green':nor_green})
        
    return df


def find_centroids(rs_image, k):
    # flatten pixel list
    pixels = rs_image.reshape((-1, 3))

    # deploy kmeans to pixels 
    n_clusters = 5
    color_k_means= KMeans(n_clusters)
    color_k_means.fit(pixels)

    # centroids value
    print(color_k_means.cluster_centers_)

    # the rgb values of centroids
    centroids_colors = np.asarray(color_k_means.cluster_centers_, dtype='uint8')
    return centroids_colors


