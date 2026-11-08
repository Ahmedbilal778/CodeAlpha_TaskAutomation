
import os
import shutil

# Source and destination folders
source_folder = "images"
destination_folder = "organized_images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Read all files from source folder
files = os.listdir(source_folder)

# Move JPG files
for file in files:

    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(file, "moved successfully!")

print("\nJPG file organization completed!")
