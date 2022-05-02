import argparse
import sys

from PIL import Image

from .core import Generator


def main():
    parser = argparse.ArgumentParser(description="Generates PJSekai background image from Image.")
    parser.add_argument("-b", "--background", help="Background image file path.", required=False, default=None)
    parser.add_argument("-f", "--format", help="Output image format.", required=False, default="png")
    parser.add_argument("base", help='Base image file path, or "-" for stdin.')
    parser.add_argument("output", help='Output image file path, or "-" for stdout.')

    args = parser.parse_args()

    if args.background:
        background = Image.open(args.background)
    else:
        background = None

    if args.base == "-":
        base = Image.open(sys.stdin.buffer)
    else:
        base = Image.open(args.base)

    generator = Generator(base=background)
    generated = generator.generate(source=base)

    if args.output == "-":
        generated.save(sys.stdout.buffer, format=args.format)
    else:
        generated.save(args.output, format=args.format)

    sys.stderr.write("Done.\n")


if __name__ == "__main__":
    main()
