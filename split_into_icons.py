import os, pathlib, shutil

if __name__ == "__main__":
	mods_dir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	icons_dir = "icons"

	for root, subdirs, png_files in os.walk(mods_dir):
		for png_filename in png_files:
			p = pathlib.Path(root)
			
			png_path = p / png_filename

			# Removes the mods_dir part and replaces it with icons_dir.
			icon_path = icons_dir / pathlib.Path(*png_path.parts[1:])

			# print(png_path)
			# print(icon_path)
			# print()

			if not os.path.isdir(icon_path.parent):
				os.makedirs(icon_path.parent)

			shutil.copyfile(src=png_path, dst=icon_path)

			subicons_path = str(icon_path.parent / icon_path.stem) + "_icons"
			if not os.path.isdir(subicons_path):
				os.mkdir(subicons_path)