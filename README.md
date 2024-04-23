# Image Processing Functions

This repository contains a collection of image processing functions implemented in Python using the PIL (Python Imaging Library) and OpenCV libraries. These functions enable various image transformations and enhancements.

## Functions

### 1. Image Negative
- **Function:** `apply_image_negative(file_path)`
- **Description:** Converts an input image to its negative version.
- **Input:** Path to the input image file.
- **Output:** Negative version of the input image.

### 2. Gamma Correction
- **Function:** `apply_gamma_correction(file_path, gamma)`
- **Description:** Applies gamma correction to the input image.
- **Input:** Path to the input image file, gamma value.
- **Output:** Image with gamma correction applied.

### 3. Logarithmic Transformation
- **Function:** `apply_logarithmic_transformation(file_path, c)`
- **Description:** Applies logarithmic transformation to the input image.
- **Input:** Path to the input image file, parameter c.
- **Output:** Transformed image.

### 4. Contrast Stretching
- **Function:** `apply_contrast_stretching(file_path)`
- **Description:** Enhances the contrast of the input image.
- **Input:** Path to the input image file.
- **Output:** Image with contrast stretched.

### 5. Histogram Equalization
- **Function:** `apply_histogram_equalization(image_path)`
- **Description:** Equalizes the histogram of the input image.
- **Input:** Path to the input image file.
- **Output:** Image with histogram equalization applied.

### 6. Intensity Level Slicing
- **Function:** `apply_intensity_level_slicing(image_path, low_threshold, high_threshold, fill_color=(255, 255, 255))`
- **Description:** Performs intensity level slicing on the input image.
- **Input:** Path to the input image file, low threshold, high threshold, fill color (optional).
- **Output:** Sliced image.

### 7. Bit Plane Slicing
- **Function:** `apply_bit_plane_slicing(image_path, bit_plane)`
- **Description:** Slices the bit planes of the input image.
- **Input:** Path to the input image file, bit plane.
- **Output:** Image with bit plane sliced.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/TigistW/Computer_Vision_Projects/image-processing-functions.git
