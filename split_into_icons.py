import os, shutil, numpy
from pathlib import Path
from PIL import Image


def create_sprite_sheet_parent_dir(sprite_sheet_path_parent):
	if not os.path.isdir(sprite_sheet_path_parent):
		os.makedirs(sprite_sheet_path_parent)


def create_icons_dir(subicons_folder_path):
	# Make a folder which will contain the icons of individual items.
	if not os.path.isdir(subicons_folder_path):
		os.mkdir(subicons_folder_path)


def create_icons(old_sprite_sheet_path, subicons_folder_path):
	atlas = Image.open(old_sprite_sheet_path)
	pix = numpy.array(atlas)

	WIDTH = 16
	HEIGHT = 16

	tiles = [pix[x:x+WIDTH, y:y+HEIGHT] for x in range(0, pix.shape[0], WIDTH) for y in range(0, pix.shape[1], HEIGHT)]

	i = 1
	for tile in tiles:
		image = Image.fromarray(tile)

		icon_path = subicons_folder_path / (str(i) + ".png")
		image.save(icon_path)

		i += 1


def crop(path, input, height, width, page, area):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                o = a.crop(area)
                o.save(os.path.join(path,"PNG","%s" % page,"IMG-%s.png" % k))
            except:
                pass

if __name__ == "__main__":
	mods_dir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	icons_dir = "generated-icons"

	for root, subdirs, png_files in os.walk(mods_dir):
		for png_filename in png_files:
			old_sprite_sheet_path = Path(root) / png_filename

			# Removes the mods_dir folder at the beginning and replaces it with icons_dir.
			sprite_sheet_path = icons_dir / Path(*old_sprite_sheet_path.parts[1:])
			sprite_sheet_path_parent = sprite_sheet_path.parent

			# Subicons are the individual items in a big item atlas png.
			subicons_folder_path = Path(str(sprite_sheet_path_parent / sprite_sheet_path.stem) + "_icons")

			create_sprite_sheet_parent_dir(sprite_sheet_path_parent)
			create_icons_dir(subicons_folder_path)
			create_icons(old_sprite_sheet_path, subicons_folder_path)