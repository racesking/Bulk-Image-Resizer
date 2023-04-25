# Bulk Image Resizer

A Python script that resizes multiple images at once, preserving their aspect ratio. This can be useful for web developers or content creators who need to optimize images for their websites or social media. The script uses the Pillow library to manipulate images.

## Dependencies

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/)

To install the Pillow library, run:

```
pip install pillow
```

## Usage

```
python bulk_image_resizer.py <input_folder> <output_folder> <max_size>
```

- `<input_folder>`: The path to the folder containing the images to be resized.
- `<output_folder>`: The path to the folder where resized images will be saved. The folder will be created if it doesn't exist.
- `<max_size>`: The maximum width and height (in pixels) for the resized images. The images will be resized while preserving their aspect ratio.

## Example

```
python bulk_image_resizer.py input_images resized_images 800
```

This command will resize all the images in the `input_images` folder and save the resized images in the `resized_images` folder. The maximum width and height for the resized images will be 800 pixels.