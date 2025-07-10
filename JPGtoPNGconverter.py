import sys
import os
from PIL import Image

# Use sys module to grab the first and second argument, which refers to folders containing .jpg files and .png files respectively.
JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]
print(JPG_folder, PNG_folder)

# Check if 'PNG_folder' exists. If not,  create it.
isExist = os.path.exists(PNG_folder)
if isExist is False:
    print(f'{PNG_folder} does not exist')
    os.makedirs(PNG_folder)
    print(f'Directory {PNG_folder} created')
else:
    print(f'{PNG_folder } does exist')

# Create a list including all .jpg files.
jpg_images = os.listdir(JPG_folder)

# Iterate over all .jpg files, convert them to .png files and store them in 'PNG_folder'.
for image_name in jpg_images:
    img = Image.open(f'{JPG_folder}/{image_name}')
    clean_name = os.path.splitext(image_name)[0]   # get the image name without the extension (.jpg)
    img.save(f'{PNG_folder}/{clean_name}.png')
print('All done!')



