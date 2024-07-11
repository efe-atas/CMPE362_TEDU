# Image Processing and 2D DCT Implementation

## Overview

This repository contains two main tasks related to image processing and mathematical transformations, implemented in Python without relying on advanced libraries (other than using OpenCV for image loading and displaying):

1. **Image Sum**: A function that combines two images by taking the maximum value of corresponding pixels.
2. **2D Discrete Cosine Transform (DCT)**: A function to perform a 2D DCT transformation on a given matrix, with optional padding to specified dimensions.

## Image Sum

### Description

The `image_sum` function takes two images as input and creates a new image where each pixel is the maximum value of the corresponding pixels from the input images. This operation is done manually using nested loops, ensuring no advanced image processing libraries are used.

### Key Steps

1. **Load Images**: Using OpenCV to read the input images.
2. **Determine Dimensions**: Extracting the height, width, and number of color channels from the images.
3. **Initialize Result Image**: Creating an empty image array to store the result.
4. **Pixel-wise Maximum Calculation**: Iterating through each pixel and each color channel to compute the maximum value.
5. **Convert to Numpy Array**: Converting the resulting image array to a format suitable for displaying with OpenCV.
6. **Display Images**: Showing the input and result images using OpenCV.

## 2D Discrete Cosine Transform (DCT)

### Description

The `dct2` function performs a 2D DCT on a given matrix. This implementation includes functions to handle 1D DCT, matrix transposition, and padding the matrix to desired dimensions. The approach ensures the transformation is done without relying on external mathematical libraries.

### Key Steps

1. **1D DCT**: Implementing a function to compute the 1D DCT of a signal.
2. **Matrix Transposition**: Creating a function to transpose a matrix.
3. **Padding the Matrix**: Implementing a function to pad the matrix to the desired number of rows and columns.
4. **2D DCT Calculation**: Applying the 1D DCT function to each row and then to each column of the transposed matrix, and finally transposing back to obtain the 2D DCT.
5. **Printing the Result**: Providing a function to print the resulting matrix with formatted values.

## Usage

To use these functions, follow the steps below:

### Image Sum

1. Load the images using OpenCV.
2. Call the `image_sum` function with the two images as arguments.
3. Display the original and resulting images using OpenCV.

### 2D DCT

1. Define a matrix for transformation.
2. Call the `dct2` function with the matrix and optional target dimensions for padding.
3. Use the provided function to print the transformed matrix.

## Requirements

- Python 3.x
- OpenCV (for image loading and displaying)

## Note

These implementations are designed to demonstrate basic image processing and mathematical transformations without using advanced libraries. They are intended for educational purposes and may not be optimized for performance on large datasets or images.
