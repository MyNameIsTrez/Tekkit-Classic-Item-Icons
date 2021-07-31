import os, shutil
from pathlib import Path


def create_sprite_sheet_parent_dir(sprite_sheet_path_parent):
	if not os.path.isdir(sprite_sheet_path_parent):
		os.makedirs(sprite_sheet_path_parent)


def create_icons_dir(subicons_folder_path):
	# Make a folder which will contain the icons of individual items.
	if not os.path.isdir(subicons_folder_path):
		os.mkdir(subicons_folder_path)


def create_icons(old_sprite_sheet_path, subicons_folder_path):
	i = 0
	for icon_image in get_icon_images(old_sprite_sheet_path):
		print(icon_image)

		icon_path = subicons_folder_path / (str(i) + ".png")
		print(icon_path)
		
		i += 1


def get_icon_images(old_sprite_sheet_path):
	yield old_sprite_sheet_path


if __name__ == "__main__":
	mods_dir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	icons_dir = "icons"

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