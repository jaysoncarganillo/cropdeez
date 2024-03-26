# Image Cropping and Scaling Script

This Python script uses the Python Imaging Library (PIL) to crop and scale images in the current working directory.

## Description

The script performs the following operations on each image file (with extensions .jpg, .jpeg, .png, .bmp, .gif, .tiff) in the current working directory:

1. Crops the image to a square shape, using the smaller dimension of the original image as the size of the square.
2. Resizes the cropped image to a 250x250 pixel image using the LANCZOS filter, a high-quality downsampling filter.
3. If the image has an alpha channel (transparency) or is a palette-based image, it converts the image to RGB.
4. Saves the new image in a 'cropped' directory with the same name as the original image but with a '.jpg' extension.

## Getting Started

### Prerequisites

You need to have Python installed on your machine along with the Python Imaging Library (PIL). You can install PIL with pip:

in bash
pip install pillow

## Usage

To use this script, simply navigate to the directory containing your images and run the script:
```python cropdeez.py```
