import cv2
import numpy as np
# Read the image
image_path = "D:/Pictures/Camera Roll/3d paint.png" 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Failed to load the image.")
else:
 # Display the original image
    cv2.imshow("Original Image", image)
 # Apply Sobel filter to extract edges
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_edges = cv2.magnitude(sobel_x, sobel_y)
    sobel_edges = cv2.normalize(sobel_edges, None, 0, 255, 
    cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Display edges extracted using Sobel filter
    cv2.imshow("Edges (Sobel Filter)", sobel_edges)
    # Apply Laplacian filter to extract edges
    laplacian_edges = cv2.Laplacian(image, cv2.CV_64F)
    laplacian_edges = cv2.normalize(laplacian_edges, None, 0, 255, 
    cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Display edges extracted using Laplacian filter
    cv2.imshow("Edges (Laplacian Filter)", laplacian_edges)
    # Apply Gaussian blur to extract textures
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
    # Display image with Gaussian blur
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
