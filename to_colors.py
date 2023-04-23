import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt



def rgb_to_hex(centroids_colors):
    '''
    centroids_colors: numpy array
    return: numpy array
    '''
    color_hex = []
    for val in centroids_colors:
        hex_val = '#{:02x}{:02x}{:02x}'.format(val[0], val[1], val[2])
        color_hex.append(hex_val)
    return color_hex



def show_colors(centroids_colors, k):
    '''
    centroids_colors: numpy array
    k: integer
    return: None
    '''

    print("Dominant"+str(k)+"Colours of Image --->")

    # plt.axis('off')
    # plt.imshow([centroids_colors])
    # plt.set_xticklabels(color_hex)
    # plt.show()
    fig, ax = plt.subplots(1,1)
    img = ax.imshow([centroids_colors])
    x_label_list = rgb_to_hex(centroids_colors)
    ax.set_xticks(range(k))
    ax.set_xticklabels(x_label_list)



def show_color_percentage(pixels, k, centroids_colors):

    # deploy kmeans to pixels
    color_k_means= KMeans(k)
    color_k_means.fit(pixels)

    # count how many pixels grouped in each color centroids
    pixels_num = np.unique(color_k_means.labels_, return_counts=True)[1]
    # calculate the percentage of each dominant colors 
    percentage = pixels_num/pixels.shape[0]
    # round to 2 decimal
    percentage = np.around(percentage, decimals = 3)

    print("Percentage: ",percentage)
    plt.title('Percentage Of Dominant Colors', size=16)
    plt.bar(range(1,k+1), percentage, color=np.array(centroids_colors)/255)
    #addlabels(range(1,n_clusters+1), percentage)
    plt.ylabel('Percentage')
    plt.xlabel('Colors')
    plt.show()



def compress_image(pixels, k, centroids_colors):
    p=pixels.copy()

    # replace each pixel color values with its centroids
    for px in range(pixels.shape[0]):
        for _ in range(centroids_colors.shape[0]):
            p[px]=centroids_colors[color_k_means.labels_[px]]
    
    # deploy kmeans to pixels
    color_k_means= KMeans(k)
    color_k_means.fit(pixels)

    # generate new image only with dominant colors
    img = p.reshape(500, -1, 3)
    cv2.imwrite("regenrated_img.png",img)

    # show resized image
    plt.subplot(122)
    plt.title('Regenerated Image using KMeans')
    plt.imshow(img)
    plt.show()



def show_img(rs_image):
    plt.figure(figsize=(14,10))
    plt.subplot(121)
    plt.title('Original Image with Decreased Pixels')
    plt.imshow(rs_image)


