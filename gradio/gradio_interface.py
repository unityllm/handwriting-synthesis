import gradio as gr
from handwriting_synthesis.hand import Hand
import tempfile
import os

def generate_handwriting(text):
    hand = Hand()
    lines = text.split('\n')
    biases = [0.75 for _ in lines]
    styles = [9 for _ in lines]
    stroke_colors = ['black' for _ in lines]
    stroke_widths = [2 for _ in lines]

    # Use a temporary file to save the output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".svg") as tmp_file:
        filename = tmp_file.name

    hand.write(
        filename=filename,
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )

    # Read the SVG content
    with open(filename, 'r') as file:
        svg_content = file.read()

    # Clean up the temporary file
    os.remove(filename)

    return svg_content

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_handwriting,
    inputs=gr.inputs.Textbox(lines=5, placeholder="Enter text here..."),
    outputs=gr.outputs.HTML(label="Generated Handwriting"),
    title="Handwriting Synthesis",
    description="Enter text to generate handwriting using a neural network model."
)

if __name__ == "__main__":
    iface.launch()
