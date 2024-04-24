from PIL import Image
import gradio as gr
import functions

# Declare input parameters for each function
gradient_input_one = [
    gr.Image(type="filepath")
    ]
gradient_input_two = [
    gr.Image(type="filepath"),
    gr.Slider(minimum=0, maximum=3, step = 0.1, label="Gamma"),
    ]
gradient_input_three = [
    gr.Image(type="filepath"),
    gr.Slider(minimum=1, maximum=255, step = 10, label="Intensity"),
    ]
gradient_input_four = [
    gr.Image(type="filepath"),
    ]
gradient_input_five = [
    gr.Image(type="filepath"),
    ]
gradient_input_six = [
    gr.Image(type="filepath"),
    gr.Number(label = "Low Threshold",  minimum = 0, maximum = 255, step = 1),
    gr.Number(label = "High Threshold", minimum = 0, maximum = 255, step = 1),
    # gr.Radio(label = "Choose an approach", choices=[("Approach 1", 1), ("Approach 2", 2)])
    ]
gradient_input_seven = [
    gr.Image(type="filepath"),
    gr.Number(label="Bit Plane", minimum = 0, maximum = 7, step = 1)
    ]

# Declare parameter output
gradient_output_one = [
     gr.Image(type="filepath")                
]
gradient_output_two = [
     gr.Image(type="filepath")                
]
gradient_output_three = [
     gr.Image(type="filepath")                
]
gradient_output_four = [
     gr.Image(type="filepath")                
]

gradient_output_five = [
     gr.Image(type="filepath"), 
     gr.Image(type="filepath")
                     
]
gradient_output_six = [
     gr.Image(type="filepath"),
     gr.Image(type="filepath")              
]
gradient_output_seven = [
     gr.Image(type="filepath")                
]

# Declare Interfaces
image_negative = gr.Interface(
    fn = functions.apply_image_negative,
    inputs = gradient_input_one,
    outputs = gradient_output_one,
    description= """
    <h2 style="color: #4CAF50;">Understanding Image Negative</h2>
    <p>An image negative is the inverse of the original image, where the brightness values are inverted. In other words, the dark areas become bright, and the bright areas become dark. This transformation is often used in image processing for enhancing contrast and revealing details that may not be visible in the original image.</p>
    <h3 style="color: #0074D9;">How it's Achieved:</h3>
    <p>To achieve the image negative, each pixel value in the image is subtracted from the maximum intensity value. For grayscale images, this is usually 255 (for 8-bit images), while for color images, it depends on the color depth (e.g., 255 for 8-bit per channel). This subtraction operation results in the inversion of brightness values, effectively creating the negative of the original image.</p>
    <p>Here's the formula for calculating the negative of a pixel value:</p>
    <blockquote>
      <p style="font-family: monospace;">negative_pixel_value = max_intensity_value - original_pixel_value</p>
    </blockquote>
    <p>This process is applied to each pixel in the image, resulting in the complete inversion of brightness values.</p>
    """,
    submit_btn = "Convert Image",
    # title="Negative of an image",
    examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
)

gamma_correction = gr.Interface(
    fn = functions.apply_gamma_correction,
    description="""
    <h2 style="color: #4CAF50;">Understanding Gamma Correction</h2>
    <p>Gamma correction is a technique used to adjust the brightness and contrast of an image by applying a non-linear transformation to the pixel values. It is commonly used in image processing to correct the perceived brightness levels and improve the overall appearance of images.</p>
    <h3 style="color: #0074D9;">What is Gamma?</h3>
    <p>Gamma (γ) is a parameter that represents the relationship between the pixel intensity values in an image and the brightness levels perceived by the human eye. It is defined as the exponent used in the gamma function:</p>
    <blockquote>
    <p style="font-family: monospace;">output_intensity = input_intensity ^ gamma</p>
    </blockquote>
    <p>A gamma value greater than 1 increases the contrast of the image, making dark areas darker and bright areas brighter. Conversely, a gamma value less than 1 decreases the contrast, making the image appear lighter overall.</p>
    <h3 style="color: #FF4136;">How Gamma Correction is Applied:</h3>
    <p>To apply gamma correction to an image, each pixel value is raised to the power of the gamma value. This non-linear transformation adjusts the brightness levels in the image to match the human perception of light. The gamma-corrected image appears more visually pleasing and true to the original scene.</p>
    <p>Here's the formula for gamma correction:</p>
    <blockquote>
    <p style="font-family: monospace;">corrected_intensity = input_intensity ^ (1 / gamma)</p>
    </blockquote>
    """,
    inputs = gradient_input_two,
    outputs = gradient_output_two, 
    submit_btn="Convert Image",
    # title="Gamma correction of an image",
   examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )

logarithmic_transformation = gr.Interface(
    fn = functions.apply_logarithmic_transformation,
    description="""
    <h2 style="color: #4CAF50;">Understanding Logarithmic Transformation</h2>

    <p>Logarithmic transformation is a technique used to enhance the visibility of details in an image by compressing the dynamic range of pixel intensities. It is commonly used in image processing to improve the visualization of low-contrast images and reveal details that may not be visible in the original image.</p>

    <h3 style="color: #0074D9;">How Logarithmic Transformation Works:</h3>

    <p>In logarithmic transformation, each pixel intensity value in the image is mapped to a new value using a logarithmic function. This function compresses the dynamic range of pixel intensities, emphasizing details in the darker regions of the image while preserving details in the brighter regions.</p>

    <p>The formula for logarithmic transformation is:</p>

    <blockquote>
    <p style="font-family: monospace;">transformed_intensity = c * log(1 + intensity)</p>
    </blockquote>

    <p>Where:</p>
    <ul>
    <li><strong>c</strong> is a constant that controls the magnitude of the transformation.</li>
    <li><strong>intensity</strong> is the original pixel intensity value.</li>
    </ul>

    <p>This transformation is applied to each pixel in the image, resulting in the logarithmically transformed image.</p>

    """,
    inputs = gradient_input_three,
    outputs = gradient_output_three, 
    submit_btn="Convert Image",
    # title="Logarithmic transformation of an image",
    examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )

contrast_scketching= gr.Interface(
    fn = functions.apply_contrast_stretching,
    description="""
    <h2 style="color: #4CAF50;">Understanding Contrast Stretching</h2>

    <p>Contrast stretching, also known as contrast enhancement, is a technique used to improve the visual quality of an image by expanding its dynamic range of pixel intensities. It aims to increase the tonal separation between different objects or features in the image, thereby enhancing its clarity and detail.</p>

    <h3 style="color: #0074D9;">How Contrast Stretching Works:</h3>

    <p>In contrast stretching, the pixel intensity values of the image are linearly scaled to occupy the full available range of intensity values. This is achieved by mapping the minimum and maximum intensity values in the original image to the minimum and maximum values of the desired intensity range, respectively.</p>

    <p>The process typically involves two steps:</p>

    <ol>
    <li><strong>Normalization:</strong> Compute the minimum and maximum intensity values in the original image.</li>
    <li><strong>Stretching:</strong> Apply a linear transformation to map the intensity values to the desired range.</li>
    </ol>

    <p>After contrast stretching, the dark areas of the image become darker, and the bright areas become brighter, resulting in improved contrast and visual clarity.</p>

""",
    inputs = gradient_input_four,
    outputs = gradient_output_four, 
    submit_btn="Convert Image",
    # title="Contrast streching of an image",
    examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )

histogram_equalization= gr.Interface(
    fn = functions.apply_histogram_equalization,
    description="""
    <h2 style="color: #4CAF50;">Understanding Histogram Equalization</h2>

    <p>Histogram equalization is a technique used to enhance the contrast and brightness of an image by redistributing its pixel intensities to cover a wider range of values. It is a popular method in image processing for improving the visual quality of images and revealing details that may not be visible in the original image.</p>

    <h3 style="color: #0074D9;">How Histogram Equalization Works:</h3>

    <p>In histogram equalization, the cumulative distribution function (CDF) of the image histogram is computed and used to redistribute the pixel intensities. This process aims to spread out the intensity values across the entire dynamic range, such that the histogram becomes more uniform.</p>

    <p>The steps involved in histogram equalization are as follows:</p>

    <ol>
    <li><strong>Compute Histogram:</strong> Calculate the histogram of the original image to determine the distribution of pixel intensities.</li>
    <li><strong>Compute Cumulative Distribution Function (CDF):</strong> Compute the cumulative sum of the histogram values to obtain the CDF.</li>
    <li><strong>Map Pixel Intensities:</strong> Map the original pixel intensities to new values using the CDF, such that the histogram becomes more uniform.</li>
    </ol>

    <p>After histogram equalization, the image exhibits improved contrast and brightness, with enhanced visual details and better utilization of the available dynamic range.</p>

    """,
    inputs = gradient_input_five,
    outputs = gradient_output_five, 
    submit_btn="Convert Image",
    # title="Histogram Equalization of an image",
     examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )
intensity_level_slicing = gr.Interface(
    fn = functions.apply_intensity_level_slicing,
    description="""
    <h2 style="color: #4CAF50;">Understanding Intensity Level Slicing</h2>

    <p>Intensity level slicing, also known as thresholding, is a technique used to selectively highlight or suppress regions of an image based on their pixel intensity values. It is commonly used in image processing for segmentation and feature extraction, allowing specific features or objects to be isolated from the background.</p>

    <h3 style="color: #0074D9;">How Intensity Level Slicing Works:</h3>

    <p>In intensity level slicing, a threshold range is defined to specify the desired intensity values to be preserved or modified. Pixels with intensity values within this range are retained or modified, while pixels outside the range are suppressed or replaced with a specified fill color.</p>

    <p>The steps involved in intensity level slicing are as follows:</p>

    <ol>
    <li><strong>Define Threshold Range:</strong> Specify the minimum and maximum intensity values to be preserved or modified.</li>
    <li><strong>Apply Thresholding:</strong> Iterate through each pixel in the image and compare its intensity value with the threshold range.</li>
    <li><strong>Modify Pixel Intensity:</strong> Preserve or modify the intensity value of pixels within the threshold range, and suppress or replace the intensity value of pixels outside the range.</li>
    </ol>

    <p>Intensity level slicing allows specific features or objects in the image to be emphasized or isolated based on their intensity values, enabling effective segmentation and analysis of image content.</p>

    """,
    inputs = gradient_input_six,
    outputs = gradient_output_six, 
    submit_btn="Convert Image",
    # title="Intensity level slicing of an image",
     examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
      ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )

bit_plane_slicing = gr.Interface(
    fn = functions.apply_bit_plane_slicing,
    description= """
    <h2 style="color: #4CAF50;">Understanding Bit-Plane Slicing</h2>

    <p>Bit-plane slicing is a technique used to extract specific bits from the binary representation of pixel intensity values in an image. It is commonly used in image processing for image compression, feature extraction, and analysis.</p>

    <h3 style="color: #0074D9;">How Bit-Plane Slicing Works:</h3>

    <p>In bit-plane slicing, each pixel intensity value in the image is represented as a binary number. Bit-plane slicing involves extracting a specific bit from each binary number, resulting in a binary image where each bit-plane represents a different level of detail or significance.</p>

    <p>The steps involved in bit-plane slicing are as follows:</p>

    <ol>
    <li><strong>Convert Pixel Intensities to Binary:</strong> Represent each pixel intensity value in the image as a binary number.</li>
    <li><strong>Extract Specific Bit:</strong> Select a specific bit (bit-plane) from each binary number to form a binary image.</li>
    </ol>

    <p>Bit-plane slicing allows the extraction of features or information at different levels of granularity, enabling efficient representation and analysis of image content.</p>
 """,
    inputs = gradient_input_seven,
    outputs = gradient_output_seven, 
    submit_btn="Convert Image",
    # title="Bit Plane Slicing of an image",
     examples=[
        ["https://i.ibb.co/zsNBJzq/grayscale.jpg"],
       ["https://i.ibb.co/Gs6FbkD/sonyrgb.jpg"],
      ["https://i.ibb.co/WHBqsVF/naturergb.jpg"],
      ["https://i.ibb.co/WNCv6FV/rgbperson.jpg"],
      ["https://i.ibb.co/3SHG8rL/grayscalewomen.jpg"],
     ["https://i.ibb.co/HTxH2nf/natuure.png"],
    ["https://i.ibb.co/WsD0zJ6/photo-2024-04-24-23-19-48.jpg"]
        
    ]
    )
demo = gr.TabbedInterface([image_negative, gamma_correction, logarithmic_transformation, contrast_scketching, histogram_equalization,intensity_level_slicing,bit_plane_slicing], ["Image Negative", "Gamma Correction", "Logarithmic Transform", "Contrast Streching", "Histogram Equalization","Intensity Level Slicing", "Bit Plane Slicing"])

if __name__ == "__main__":
    demo.launch()