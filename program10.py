import cv2
# Read the image
image_path = "D:/Pictures/Camera Roll/3d paint.png" 
image = cv2.imread(image_path)
if image is None:
    print("Failed to load the image.")
else:
 # Display the original image
    cv2.imshow("Original Image", image)
    # Apply blur to the image
    blur_kernel_size = (5, 5) # Kernel size for blur filter
    blurred_image = cv2.blur(image, blur_kernel_size)
    # Display the blurred image
    cv2.imshow("Blurred Image", blurred_image)
    # Apply Gaussian blur to the image
    gaussian_blur_kernel_size = (5, 5) # Kernel size for Gaussian blur filter
    gaussian_blurred_image = cv2.GaussianBlur(image, gaussian_blur_kernel_size,0)
    # Display the Gaussian blurred image
    cv2.imshow("Gaussian Blurred Image", gaussian_blurred_image)
    # Apply median blur to the image
    median_blur_kernel_size = 5 # Kernel size for median blur filter 
    median_blurred_image = cv2.medianBlur(image, median_blur_kernel_size)
    # Display the median blurred image
    cv2.imshow("Median Blurred Image", median_blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

