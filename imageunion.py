import cv2
def image_sum(img1, img2):
   
    
    # Get the dimensions of the images
    height = len(img1)
    width = len(img1[0])
    channels = len(img1[0][0])
    
    # Manually create an image array using nested loops
    result_img = [[[0] * channels for _ in range(width)] for __ in range(height)]

    # Iterate over each pixel and each channel
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                result_img[i][j][k] = max(img1[i][j][k], img2[i][j][k])

    # Convert the list of lists of lists to a numpy array
    # It is necesarry for imshow representation
    import numpy as np
    result_image_array = np.array(result_img, dtype=np.uint8)

    return result_image_array


''''

# Load images
img1 = cv2.imread('11.jpg')
img2 = cv2.imread('12.jpg')

# Calculate result image
result_image = image_sum(img1, img2)

# Display first image
cv2.imshow('Image 1', img1)

# Display second image
cv2.imshow('Image 2', img2)

# Display result image
cv2.imshow('Result Image', result_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

'''