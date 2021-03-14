import os, pathlib, shutil


def create_sprite_sheet_parent_dir(icons_png_path):
	if not os.path.isdir(icons_png_path.parent):
		os.makedirs(icons_png_path.parent)


def create_icons_dir(icons_png_path):
	# Make a folder which will contain the icons of individual items.
	subicons_folder_path = str(icons_png_path.parent / icons_png_path.stem) + "_icons"
	if not os.path.isdir(subicons_folder_path):
		os.mkdir(subicons_folder_path)


if __name__ == "__main__":
	mods_dir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	icons_dir = "icons"

	for root, subdirs, png_files in os.walk(mods_dir):
		for png_filename in png_files:
			png_path = pathlib.Path(root) / png_filename

			# Removes the mods_dir folder at the beginning and replaces it with icons_dir.
			icons_png_path = icons_dir / pathlib.Path(*png_path.parts[1:])

			create_sprite_sheet_parent_dir(icons_png_path)
			create_icons_dir(icons_png_path)