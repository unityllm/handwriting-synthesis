import argparse
from handwriting_synthesis.hand import Hand

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate handwriting samples from text input.')
    parser.add_argument('text', type=str, nargs='+', help='Text to be converted into handwriting.')
    parser.add_argument('--biases', type=float, nargs='+', default=None, help='Bias values for each line of text.')
    parser.add_argument('--styles', type=int, nargs='+', default=None, help='Style indices for each line of text.')
    parser.add_argument('--stroke_colors', type=str, nargs='+', default=None, help='Stroke colors for each line of text.')
    parser.add_argument('--stroke_widths', type=int, nargs='+', default=None, help='Stroke widths for each line of text.')
    parser.add_argument('--output', type=str, default='output.svg', help='Output filename for the generated handwriting sample.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    hand = Hand()
    
    # Join the text arguments into lines
    lines = [' '.join(args.text)]
    
    # Generate handwriting samples
    hand.write(
        filename=args.output,
        lines=lines,
        biases=args.biases,
        styles=args.styles,
        stroke_colors=args.stroke_colors,
        stroke_widths=args.stroke_widths
    )

if __name__ == '__main__':
    main()
