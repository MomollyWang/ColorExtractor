from .to_colors import *
from .image_process import *


def extract_color(image, k):
    
    rs_image = resize(image)
    df  = pixelize(rs_image)
    elbow(df)
     # flatten pixel list
    pixels = rs_image.reshape((-1, 3))
    color_k_means = find_centroids(pixels, k)
    centroids_colors = np.asarray(color_k_means.cluster_centers_, dtype='uint8')
    show_colors(centroids_colors, k)
    show_color_percentage(pixels, k, color_k_means,centroids_colors)
    
    show_img(rs_image)
    compress_image(pixels, color_k_means, centroids_colors)


