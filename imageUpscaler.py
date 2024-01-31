from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def upscale_to_4k(input_path):
    # Define 4K resolution
    resolution_4k_width, resolution_4k_height = 3840, 2160

    # Open the image
    with Image.open(input_path) as img:
        # Calculate the new size, maintaining the aspect ratio
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height
        new_width, new_height = resolution_4k_width, resolution_4k_height

        if aspect_ratio > 1:  # Wide image
            new_height = int(new_width / aspect_ratio)
        else:  # Tall image
            new_width = int(new_height * aspect_ratio)

        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Define the output path
        directory = os.path.dirname(input_path)
        file_extension = os.path.splitext(input_path)[1]
        output_path = os.path.join(directory, f"Upscaled_Image{file_extension}")

        # Save the upscaled image
        img_resized.save(output_path)

        return output_path

def main():
    root = tk.Tk()
    root.withdraw()

    # Ask user to select an image file
    input_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpeg;*.jpg;*.png;*.bmp;*.gif")])
    if not input_path:
        print("No file selected.")
        return

    # Upscale the image
    output_path = upscale_to_4k(input_path)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    main()
