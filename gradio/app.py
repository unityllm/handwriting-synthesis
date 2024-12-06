import gradio as gr
from demo import Hand
import os

def generate_handwriting(text, styles, biases, stroke_colors, stroke_widths):
    # Ensure the output directory exists
    output_dir = 'gradio_output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the output file path
    output_file = os.path.join(output_dir, 'handwriting.svg')
    
    # Create an instance of the Hand class
    hand = Hand()
    
    # Generate the handwriting
    hand.write(
        filename=output_file,
        lines=text.split('\n'),
        biases=[float(bias) for bias in biases.split(',')],
        styles=[int(style) for style in styles.split(',')],
        stroke_colors=stroke_colors.split(','),
        stroke_widths=[int(width) for width in stroke_widths.split(',')]
    )
    
    # Return the path to the generated SVG
    return output_file

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_handwriting,
    inputs=[
        gr.inputs.Textbox(lines=5, placeholder="Enter text here..."),
        gr.inputs.Textbox(default="9,9,9,9", label="Styles (comma-separated)"),
        gr.inputs.Textbox(default="0.5,0.5,0.5,0.5", label="Biases (comma-separated)"),
        gr.inputs.Textbox(default="black,black,black,black", label="Stroke Colors (comma-separated)"),
        gr.inputs.Textbox(default="2,2,2,2", label="Stroke Widths (comma-separated)")
    ],
    outputs=gr.outputs.Image(type="file", label="Generated Handwriting"),
    title="Handwriting Synthesis",
    description="Generate handwriting from text input with customizable styles, biases, stroke colors, and widths."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
