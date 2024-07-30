import cv2
# Function to split the image into four quadrants
def split_image(image):
    height, width, _ = image.shape
    half_height = height // 2
    half_width = width // 2
 # Split the image into four quadrants
    top_left = image[:half_height, :half_width]
    top_right = image[:half_height, half_width:]
    bottom_left = image[half_height:, :half_width]
    bottom_right = image[half_height:, half_width:]
    return top_left, top_right, bottom_left, bottom_right
# Function to display images
def display_images(images, window_names):
    for img, name in zip(images, window_names):
        cv2.imshow(name, img)
    print("Press any key to terminate.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Read the image
image_path = "D:/Pictures/Camera Roll/3d paint.png" 
image = cv2.imread(image_path)
if image is None:
    print("Failed to load the image.")
else:
 # Split the image into quadrants
    top_left, top_right, bottom_left, bottom_right = split_image(image)
 # Display the quadrants
    display_images([top_left, top_right, bottom_left, bottom_right], ["Top Left", "Top Right", "Bottom Left", "Bottom Right"])
