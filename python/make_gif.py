# make_gif.py

import glob

def make_gif(image_dir):
    print("Making a gif using images from \"{0}\".".format(image_dir))

def main():
    image_dir = "images/The_KU_Tree"
    make_gif(image_dir)

if __name__ == '__main__':
    main()

