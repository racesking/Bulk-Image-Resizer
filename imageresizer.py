import os
import sys
import argparse
from PIL import Image

def resize_images(input_folder, output_folder, max_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(input_folder, filename))
            img.thumbnail(max_size)
            img.save(os.path.join(output_folder, filename))

def main():
    parser = argparse.ArgumentParser(description="Bulk Image Resizer")
    parser.add_argument("input_folder", help="Path to the folder containing the images to be resized")
    parser.add_argument("output_folder", help="Path to the folder where resized images will be saved")
    parser.add_argument("max_size", type=int, help="Maximum width and height (in pixels) for the resized images")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    max_size = (args.max_size, args.max_size)

    resize_images(input_folder, output_folder, max_size)

if __name__ == '__main__':
    main()
