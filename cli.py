import argparse
from demo import Hand

def main():
    parser = argparse.ArgumentParser(description='Generate handwriting synthesis from text input.')
    parser.add_argument('text', nargs='+', help='Text to be converted into handwriting.')
    parser.add_argument('--output', required=True, help='Output file name for the generated SVG.')
    parser.add_argument('--biases', nargs='*', type=float, default=None, help='List of biases for each line of text.')
    parser.add_argument('--styles', nargs='*', type=int, default=None, help='List of styles for each line of text.')
    parser.add_argument('--stroke_colors', nargs='*', default=None, help='List of stroke colors for each line of text.')
    parser.add_argument('--stroke_widths', nargs='*', type=int, default=None, help='List of stroke widths for each line of text.')

    args = parser.parse_args()

    # Ensure the number of biases, styles, stroke_colors, and stroke_widths match the number of lines
    num_lines = len(args.text)
    if args.biases and len(args.biases) != num_lines:
        raise ValueError("Number of biases must match the number of lines of text.")
    if args.styles and len(args.styles) != num_lines:
        raise ValueError("Number of styles must match the number of lines of text.")
    if args.stroke_colors and len(args.stroke_colors) != num_lines:
        raise ValueError("Number of stroke colors must match the number of lines of text.")
    if args.stroke_widths and len(args.stroke_widths) != num_lines:
        raise ValueError("Number of stroke widths must match the number of lines of text.")

    hand = Hand()
    hand.write(
        filename=args.output,
        lines=args.text,
        biases=args.biases,
        styles=args.styles,
        stroke_colors=args.stroke_colors,
        stroke_widths=args.stroke_widths
    )

if __name__ == '__main__':
    main()
