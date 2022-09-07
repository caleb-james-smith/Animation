# make_gif.py

import time
import os
import glob
from PIL import Image

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

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

def run():
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

def main():
    run()

if __name__ == '__main__':
    main()

