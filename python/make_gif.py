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
def combineImages(files, output_file):
    images = [Image.open(f) for f in files]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height  = max(heights)
    
    #print("total_width  = {0}".format(total_width))
    #print("max_height   = {0}".format(max_height))
    
    new_image = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]
    new_image.save(output_file)

# create gif of all images in a directory
def make_gif(image_dir, output_dir, output_file, frame_duration):
    output_path = "{0}/{1}".format(output_dir, output_file)
    images      = glob.glob(image_dir + "/*.jpg")
    
    makeDir(output_dir)
    images.sort()
    n_images = len(images)
    
    print("Making a gif using images from \"{0}\".".format(image_dir))
    print("Number of images: {0}".format(n_images))

    for image in images:
        print(image)
    
    frames      = [Image.open(image) for image in images]
    first_frame = frames[0]
    first_frame.save(output_path, format="GIF", append_images=frames, save_all=True, duration=frame_duration, loop=0)
    
    print("Output file: {0}".format(output_path))

# create combined images
# - assumes that files with the same base file names exist in both directories
# - images with same base file name are combined 
def create_combined(image_dir_1, image_dir_2, output_dir):
    print("Creating combined images.")
    images_1 = glob.glob(image_dir_1 + "/*.jpg")
    images_2 = glob.glob(image_dir_2 + "/*.jpg")
    
    makeDir(output_dir)
    images_1.sort()
    images_2.sort()
    n_images_1 = len(images_1)
    n_images_2 = len(images_2)
    
    # check that the same number of images are found
    if n_images_1 != n_images_2:
        print("ERROR: Different number of images found!")
        print(" - image_dir_1: {0}".format(image_dir_1))
        print(" - image_dir_2: {0}".format(image_dir_2))
        print(" - n_images_1:  {0}".format(n_images_1))
        print(" - n_images_2:  {0}".format(n_images_2))
        return
    
    for i1, i2 in zip(images_1, images_2):
        files   = [i1, i2]
        name_1  = os.path.basename(i1)
        name_2  = os.path.basename(i2)
        
        # check that file names match
        if name_1 != name_2:
            print("ERROR: File names do not match!")
            print(" - name_1: {0}".format(name_1))
            print(" - name_2: {0}".format(name_2))
            return

        output_file = "{0}/{1}".format(output_dir, name_1)
        combineImages(files, output_file)
        
        print(name_1)
    
    print("Output directory: {0}".format(output_dir))

# test combineImages()
def test_combine():
    files = [
        "images/The_KU_Tree_2022_09_06_v1/west_side/PXL_20220809_001.jpg",
        "images/The_KU_Tree_2022_09_06_v1/east_side/PXL_20220809_001.jpg",
    ]
    output_file = "test_combine_1.jpg"
    combineImages(files, output_file)

# combine images from input directories
def run_combine():
    # order images from left to right
    image_dir_1 = "images/The_KU_Tree_2022_09_06_v1/west_side"
    image_dir_2 = "images/The_KU_Tree_2022_09_06_v1/east_side"
    output_dir  = "images/The_KU_Tree_2022_09_06_v1/combined"
    create_combined(image_dir_1, image_dir_2, output_dir)

# create gifs of files in directory
def run_standard():
    # frame duration in milliseconds
    frame_duration = 1000
    # output directory
    output_dir  = "gifs"
    
    # all original images of tree
    image_dir   = "images/The_KU_Tree_2022_09_06_v1/original"
    output_file = "The_KU_Tree_2022_09_06_v1_original.gif"
    make_gif(image_dir, output_dir, output_file, frame_duration)
    
    # west side of tree 
    image_dir   = "images/The_KU_Tree_2022_09_06_v1/west_side"
    output_file = "The_KU_Tree_2022_09_06_v1_west_side.gif"
    make_gif(image_dir, output_dir, output_file, frame_duration)
    
    # east side of tree 
    image_dir   = "images/The_KU_Tree_2022_09_06_v1/east_side"
    output_file = "The_KU_Tree_2022_09_06_v1_east_side.gif"
    make_gif(image_dir, output_dir, output_file, frame_duration)
    
    # combined west side and east side images of tree
    image_dir   = "images/The_KU_Tree_2022_09_06_v1/combined"
    output_file = "The_KU_Tree_2022_09_06_v1_combined.gif"
    make_gif(image_dir, output_dir, output_file, frame_duration)

# main
def main():
    start_time = time.time()
    
    test_combine()
    run_combine()
    run_standard()
    
    end_time = time.time()
    
    run_time = end_time - start_time
    
    print("run time: {0:.3f} seconds".format(run_time))

if __name__ == '__main__':
    main()

