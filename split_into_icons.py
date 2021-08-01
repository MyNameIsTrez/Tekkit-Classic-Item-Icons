import os, shutil
from pathlib import Path
from PIL import Image
import numpy as np


def create_sprite_sheet_parent_dir(sprite_sheet_path_parent):
	if not os.path.isdir(sprite_sheet_path_parent):
		os.makedirs(sprite_sheet_path_parent)


def create_icons_dir(subicons_folder_path):
	# Make a folder which will contain the icons of individual items.
	if not os.path.isdir(subicons_folder_path):
		os.mkdir(subicons_folder_path)


def create_icons(old_sprite_sheet_path, subicons_folder_path):
	atlas = Image.open(old_sprite_sheet_path)
	pix = np.array(atlas)

	WIDTH = 16
	HEIGHT = 16

	tiles = [pix[x:x+WIDTH, y:y+HEIGHT] for x in range(0, pix.shape[0], WIDTH) for y in range(0, pix.shape[1], HEIGHT)]

	i = 1
	for tile in tiles:		
		if is_valid_image(tile, old_sprite_sheet_path):
			image = Image.fromarray(tile).convert("RGBA")

			icon_path = subicons_folder_path / (str(i) + ".png")
			image.save(icon_path, "PNG")

			i += 1


def is_valid_image(tile, old_sprite_sheet_path):
	all_alpha_transparent = True
	all_purple_transparent = True

	if tile.ndim == 2: # If the 16x16 image is indexed.
		return True

	for row in tile:
		for pixel in row:
			if len(pixel) == 3: # If there's no alpha value.
				all_alpha_transparent = False

				if not np.array_equal(pixel, [214, 127, 255]) and not np.array_equal(pixel, [107, 63, 127]):
					all_purple_transparent = False
			else:
				# Checking alpha value is non-zero.
				if pixel[3] != 0:
					all_alpha_transparent = False

				# Checking inner purple color first as it's more common, then checking the outer purple color.
				if not np.array_equal(pixel, [214, 127, 255, 255]) and not np.array_equal(pixel, [107, 63, 127, 255]):
					all_purple_transparent = False

	if all_alpha_transparent or all_purple_transparent:
		return False

	return True


if __name__ == "__main__":
	mods_dir = "mods"
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