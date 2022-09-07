# make_gif.py

import time
import os
import glob
from PIL import Image

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# combine image file into a single image
def combineImages(files):
    images = [Image.open(f) for f in files]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height  = max(heights)
    
    print("total_width  = {0}".format(total_width))
    print("max_height   = {0}".format(max_height))
    
    new_image = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]
    new_image.save("combined_example_1.jpg")

# create gif of all images in a directory
def make_gif(image_dir, output_dir, output_file):
    output_path = "{0}/{1}".format(output_dir, output_file)
    images      = glob.glob(image_dir + "/*.jpg")
    
    makeDir(output_dir)
    images.sort()
    n_images = len(images)
    
    print("Making a gif using images from \"{0}\".".format(image_dir))
    print("Number of images: {0}".format(n_images))

    for image in images:
        print(image)
    
    duration    = 500
    frames      = [Image.open(image) for image in images]
    first_frame = frames[0]
    first_frame.save(output_path, format="GIF", append_images=frames, save_all=True, duration=duration, loop=0)
    
    print("Output file: {0}".format(output_path))

def run_standard():
    start_time = time.time()
    
    # all images of tree
    image_dir   = "images/The_KU_Tree_2022_09_06_v1"
    output_dir  = "gifs"
    output_file = "The_KU_Tree_2022_09_06_v1.gif"
    make_gif(image_dir, output_dir, output_file)
    
    # west side of tree 
    image_dir   = "images/The_KU_Tree_2022_09_06_v1_split/west_side"
    output_dir  = "gifs"
    output_file = "The_KU_Tree_2022_09_06_v1_west_side.gif"
    make_gif(image_dir, output_dir, output_file)
    
    # east side of tree 
    image_dir   = "images/The_KU_Tree_2022_09_06_v1_split/east_side"
    output_dir  = "gifs"
    output_file = "The_KU_Tree_2022_09_06_v1_east_side.gif"
    make_gif(image_dir, output_dir, output_file)
    
    end_time = time.time()
    
    run_time = end_time - start_time
    
    print("run time: {0:.3f} seconds".format(run_time))

def run_combined():
    files = [
        "images/The_KU_Tree_2022_09_06_v1_split/west_side/PXL_20220809_001.jpg",
        "images/The_KU_Tree_2022_09_06_v1_split/east_side/PXL_20220809_001.jpg",
    ]
    combineImages(files)

def main():
    #run_standard()
    run_combined()

if __name__ == '__main__':
    main()

