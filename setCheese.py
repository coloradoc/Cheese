import os
from PIL import Image


# Get the user's home directory and the desktop folder
home_dir = os.path.expanduser(r"C:\Users\FRC")
desktop_dir = os.path.join(home_dir, "Desktop")

# Set the directory containing the images
image_dir = r"C:\Users\FRC\Desktop\Cheese-main\dataset\cheese"

# Iterate over the files in the directory
for filename in os.listdir(image_dir):
    # Filter out non-image files
    if not filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        continue

    # Load the image
    image_path = os.path.join(image_dir, filename)
    image = Image.open(image_path)

    # Save the image to the desktop folder
    desktop_path = os.path.join(desktop_dir, filename)
    image.save(desktop_path)

    # Optional: print a message indicating that the file was saved
    print(f"Saved {filename} to desktop")
