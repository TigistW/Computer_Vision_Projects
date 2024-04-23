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
    gr.Slider(minimum=0, maximum=254, step = 10, label="Intensity"),
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
     gr.Image(type="filepath")                
]
gradient_output_six = [
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
    submit_btn = "Convert Image",
    title="Negative of an image",
    # examples=
    # [
    #     ["Tge.jpg"],
    #     ["Sosna.jpg",],    
    # ]
    )

gamma_correction = gr.Interface(
    fn = functions.apply_gamma_correction,
    inputs = gradient_input_two,
    outputs = gradient_output_two, 
    submit_btn="Convert Image",
    title="Gamma correction of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )

logarithmic_transformation = gr.Interface(
    fn = functions.apply_logarithmic_transformation,
    inputs = gradient_input_three,
    outputs = gradient_output_three, 
    submit_btn="Convert Image",
    title="Logarithmic transformation of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )

contrast_scketching= gr.Interface(
    fn = functions.apply_contrast_stretching,
    inputs = gradient_input_four,
    outputs = gradient_output_four, 
    submit_btn="Convert Image",
    title="Contrast streching of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )

histogram_equalization= gr.Interface(
    fn = functions.apply_histogram_equalization,
    inputs = gradient_input_five,
    outputs = gradient_output_five, 
    submit_btn="Convert Image",
    title="Histogram Equalization of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )
intensity_level_slicing = gr.Interface(
    fn = functions.apply_intensity_level_slicing,
    inputs = gradient_input_six,
    outputs = gradient_output_six, 
    submit_btn="Convert Image",
    title="Intensity level slicing of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )

bit_plane_slicing = gr.Interface(
    fn = functions.apply_bit_plane_slicing,
    inputs = gradient_input_seven,
    outputs = gradient_output_seven, 
    submit_btn="Convert Image",
    title="Bit Plane Slicing of an image",
    # examples=
    # [
    #     ["../Tge.jpg"],
    #     ["../Sosna.jpg",],    
    # ]
    )
demo = gr.TabbedInterface([image_negative, gamma_correction, logarithmic_transformation, contrast_scketching, histogram_equalization,intensity_level_slicing,bit_plane_slicing], ["Image Negative", "Gamma Correction", "Logarithmic_transform", "Contrast Streching", "Histogram Equalization","Intensity Level Slicing", "Bit Plane Slicing"])

if __name__ == "__main__":
    demo.launch()