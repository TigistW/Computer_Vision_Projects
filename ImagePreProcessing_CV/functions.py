from PIL import Image
import numpy as np
import cv2
def apply_image_negative(file_path):
    image = Image.open(file_path)
    width, height = image.size
    
    # Create a new image with the same mode as the input image
    negative_image = Image.new(image.mode, (width, height))  

    for x in range(width):
        for y in range(height):
            if image.mode == 'RGB':
                r, g, b = image.getpixel((x, y))
                negative_image.putpixel((x, y), (255 - r, 255 - g, 255 - b))
                
            elif image.mode == 'L':
                intensity = image.getpixel((x, y))
                negative_intensity = 255 - intensity
                negative_image.putpixel((x, y), negative_intensity)
                
            else:
                
                raise ValueError("Unsupported image mode: {}".format(image.mode))

    return negative_image

def apply_gamma_correction(file_path, gamma):
    image = Image.open(file_path)
    width, height = image.size
    corrected_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            if image.mode == 'RGB': 
                r, g, b = image.getpixel((x, y))
                r_corrected = int(255 * (r / 255) ** gamma)
                g_corrected = int(255 * (g / 255) ** gamma)
                b_corrected = int(255 * (b / 255) ** gamma)
                corrected_image.putpixel((x, y), (r_corrected, g_corrected, b_corrected))
                
            elif image.mode == 'L': 
                intensity = image.getpixel((x, y))
                intensity_corrected = int(255 * (intensity / 255) ** gamma)
                corrected_image.putpixel((x, y), intensity_corrected)
            else:
                raise ValueError("Unsupported image mode: {}".format(image.mode))
            

    return corrected_image

def apply_logarithmic_transformation(file_path, c):
    image = Image.open(file_path)
    width, height = image.size
    transformed_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            if image.mode == 'RGB':  # If the mode is RGB
                r, g, b = image.getpixel((x, y))
                # Apply logarithmic transformation to each channel
                r_transformed = int(c * np.log1p(1 + r))  # Apply logarithmic transformation to the red channel
                g_transformed = int(c * np.log1p(1 + g))  # Apply logarithmic transformation to the green channel
                b_transformed = int(c * np.log1p(1 + b))  # Apply logarithmic transformation to the blue channel
                transformed_image.putpixel((x, y), (r_transformed, g_transformed, b_transformed))
            elif image.mode == 'L':  # If the mode is grayscale
                intensity = image.getpixel((x, y))
                intensity_transformed = int(c * np.log1p(1 + intensity))  # Apply logarithmic transformation to the intensity
                transformed_image.putpixel((x, y), intensity_transformed)
            else:
                raise ValueError("Unsupported image mode: {}".format(image.mode))  # Raise error for unsupported image modes

    return transformed_image
def apply_contrast_stretching(file_path):
    image = Image.open(file_path)
    width, height = image.size
    stretched_image = Image.new(image.mode, (width, height))  # Create a new image with the specified mode

    if image.mode == 'RGB':
        num_bands = 3 
    elif image.mode == 'L':
        num_bands = 1 

    # Initialize min_val and max_val lists for each band
    min_val = [255] * num_bands 
    max_val = [0] * num_bands   

    # Calculate minimum and maximum pixel values
    for x in range(width):
        for y in range(height):
            pixel_values = image.getpixel((x, y))
            min_val = [min(v, p) for v, p in zip(min_val, pixel_values)]  # Update min values
            max_val = [max(v, p) for v, p in zip(max_val, pixel_values)]  # Update max values

    # Apply contrast stretching
    for x in range(width):
        for y in range(height):
            pixel_values = image.getpixel((x, y))
            stretched_values = tuple(int(255 * (p - min_v) / (max_v - min_v)) for p, min_v, max_v in zip(pixel_values, min_val, max_val))
            stretched_image.putpixel((x, y), stretched_values)

    return stretched_image

def apply_histogram_equalization(image_path):
    img = cv2.imread(image_path)

    # Check if the image is in grayscale or RGBa format
    if len(img.shape) == 2:  # Grayscale image
        equalized_img = cv2.equalizeHist(img)
    elif len(img.shape) == 3 and img.shape[2] == 3:  # RGB image
        # Convert RGB image to YUV color space
        yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        
        # Apply histogram equalization to the Y channel
        yuv_img[:,:,0] = cv2.equalizeHist(yuv_img[:,:,0])
        
        # Convert back to RGB color space
        equalized_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
    else:
        raise ValueError("Unsupported image format")

    return equalized_img

def apply_intensity_level_slicing(image_path, low_threshold, high_threshold, fill_color=(255, 255, 255)):
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image is in grayscale or RGBa format
    if len(img.shape) == 2:  # Grayscale image
  
        mask = cv2.inRange(img, low_threshold, high_threshold)
        img_sliced = np.where(mask != 0, img, fill_color)
    elif len(img.shape) == 3 and img.shape[2] == 3:  # RGB image
        # Convert RGB image to HSV color space
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Apply intensity level slicing to the V channel
        mask = cv2.inRange(hsv_img[:,:,2], low_threshold, high_threshold)
        hsv_img[:,:,2] = np.where(mask != 0, hsv_img[:,:,2], fill_color[2])
        
        # Convert back to RGB color space
        img_sliced = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    else:
        raise ValueError("Unsupported image format")

    return img_sliced

def apply_bit_plane_slicing(image_path, bit_plane):
    # Read the image
    img = cv2.imread(image_path)

    if len(img.shape) == 2: 
        bit_plane_img = (img >> bit_plane) & 1
    elif len(img.shape) == 3 and img.shape[2] == 3:
        
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bit_plane_img = (gray_img >> bit_plane) & 1
    else:
        raise ValueError("Unsupported image format")

    bit_plane_img = bit_plane_img * 255

    return bit_plane_img


