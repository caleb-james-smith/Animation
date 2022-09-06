# make_gif.py

import os
import glob
from PIL import Image

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def make_gif(image_dir, output_dir, output_file):
    output_name = "{0}/{1}".format(output_dir, output_file)
    images      = glob.glob(image_dir + "/*.jpg")
    
    makeDir(output_dir)
    images.sort()
    n_images = len(images)
    
    print("Making a gif using images from \"{0}\".".format(image_dir))
    print("Number of images: {0}".format(n_images))
    
    frames      = [Image.open(image) for image in images]
    first_frame = frames[0]
    first_frame.save(output_name, format="GIF", append_images=frames, save_all=True, duration=100, loop=0)

def main():
    image_dir   = "images/The_KU_Tree"
    output_dir  = "gifs"
    output_file = "The_KU_Tree.gif"
    make_gif(image_dir, output_dir, output_file)

if __name__ == '__main__':
    main()

