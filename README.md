# Animation
Create animations (gifs, etc.).

## Instructions

### Setup
Download repository:
```
git clone git@github.com:caleb-james-smith/Animation.git
cd Animation
```
Create an album (e.g. Google photos album), download, move, unzip, and rename.
```
mkdir -p images
cd images
mv ~/Downloads/The_KU_Tree-001.zip .
unzip The_KU_Tree-001.zip
mv The_KU_Tree The_KU_Tree_2022_09_06_v1
cd ..
```
You can then organize the images into different categories using directories (e.g. original, west side, east side, ...) and rename files.
When combining images in different directories, images with the same base file name will be combined.
For gifs, images are sorted by full file name.

### Running
Run this python script to create combined images and gifs.
You will need to modify directory paths first.
```
python3 python/make_gif.py
```
