from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb):
    # Open the image file
    img = Image.open(input_path)

    # Calculate the target size in bytes (1 KB = 1024 bytes)
    target_size_bytes = target_size_kb * 1024

    # Compress the image until its size is less than the target size
    quality = 90  # Initial quality value (adjust as needed)
    while True:
        # Save the image with the current quality
        img.save(output_path, optimize=True, quality=quality)

        # Check the size of the saved image
        file_size = os.path.getsize(output_path)

        # Stop compressing if the image is below the target size
        if file_size <= target_size_bytes:
            break

        # Reduce the quality for the next iteration
        quality -= 5
        if quality < 10:
            break  # Ensure minimum quality level
    
    return output_path

    
# # Example usage:
# input_image_path = "input_image.jpg"
# output_image_path = "compressed_image.jpg"
# target_size_kb = 800  # Target size in KB

# # Compress the image
# compress_image(input_image_path, output_image_path, target_size_kb)
