# Color Palette Extractor 

Our project focuses on extracting color pallete of an image using  KMeans clustering algorithm. The basic idea is to treat each pixel in the image as a data point with a three-dimensional feature vector representing the pixel's RGB values. Then, the k-means algorithm is applied to cluster the data points into k clusters, where k is a pre-defined parameter. The resulting cluster centers represent the dominant colors in the image.

Here's an example about how this extractor works. We use a painting by Monet as the input image.

In this extractor, we handle input image by resizing it first. 

![download](https://user-images.githubusercontent.com/105327885/233823899-b23c7ec7-9cf1-4490-8fc8-b65f81c0813f.png)

Then we go through each pixels, use k-means to find the most dominant k colors. Here we set k = 5:

![download-1](https://user-images.githubusercontent.com/105327885/233823950-c60854b4-d936-43db-b43a-a70f5229aa09.png)

After that, we regenerate image with only dominant colors. We achieve this by replacing each pixel with its centroid color. You can see the result below:

![download-2](https://user-images.githubusercontent.com/105327885/233824030-69b4fa21-b62d-4b3d-8043-27c0c0bc9059.png)
