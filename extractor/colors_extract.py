from to_colors import show_colors, show_color_percentage, compress_image, show_img
from image_process import resize, pixelize, find_centroids
import matplotlib.pyplot as plt

def extract_color(image, k):
    
    rs_image = resize(image)
    pixels  = pixelize(rs_image)
    centroids_colors = find_centroids(rs_image, k)

    show_colors(centroids_colors, k)
    show_color_percentage(pixels, k, centroids_colors)
    
    show_img(rs_image)
    compress_image(pixels, k, centroids_colors)


