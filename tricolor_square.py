from PIL import Image, ImageDraw

# Define colors using hex codes

red = "#FF0000"
green = "#00FF00"
blue = "#0000FF"

# Create a new image with a white background
image = Image.new("RGB", (300, 100), "white")
draw = ImageDraw.Draw(image)

# Define the coordinates for the color blocks
red_block = (0, 0, 100, 100)
green_block = (100, 0, 200, 100)
blue_block = (200, 0, 300, 100)

# Draw color blocks with specified colors
draw.rectangle(red_block, fill=red)
draw.rectangle(green_block, fill=green)
draw.rectangle(blue_block, fill=blue)

# Save and display the image
image.show()
