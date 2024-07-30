import cv2
import numpy as np
# Read the image
image_path = "D:/Pictures/Camera Roll/3d paint.png" 
image = cv2.imread(image_path)
if image is None:
    print("Failed to load the image.")
else:
 # Display the original image
    cv2.imshow("Original Image", image)
 # Rotation
    angle = 45 # Rotation angle in degrees
    center = (image.shape[1] // 2, image.shape[0] // 2) # Center of rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0) # Rotation 
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1],image.shape[0]))
 # Scaling
    scale_factor = 0.5 # Scaling factor (0.5 means half the size)
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
 # Translation
    translation_matrix = np.float32([[1, 0, 100], [0, 1, -50]]) # Translation matrix 
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1],image.shape[0]))
 # Display the transformed images
    cv2.imshow("Rotated Image", rotated_image)
    cv2.imshow("Scaled Image", scaled_image)
    cv2.imshow("Translated Image", translated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
