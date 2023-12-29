from PIL import Image

def convert_to_black_and_white(image_path, threshold):
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')

    # Apply thresholding to create a black and white image
    black_and_white_image = image.point(lambda x: 0 if x < threshold else 255, '1')

    return black_and_white_image

# Specify the path to your image
image_path = "floor_0.png"

# Set the threshold value for black and white conversion
threshold_value = 128

# Convert the image to black and white
result_image = convert_to_black_and_white(image_path, threshold_value)

# Display the resulting black and white image
#result_image.show()

# Save the resulting image
output_path = "floor_0(result).png"
result_image.save(output_path)

