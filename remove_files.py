import os, zipfile


def remove_empty_folders(path, remove_root=True):
	if not os.path.isdir(path):
		return

	# Remove empty subfolders.
	files = os.listdir(path)
	if len(files):
		for f in files:
			fullpath = os.path.join(path, f)
			if os.path.isdir(fullpath):
				remove_empty_folders(fullpath)

	# If the folder is empty, remove it.
	files = os.listdir(path)
	if len(files) == 0 and remove_root:
		print("Removing empty folder:", path)
		os.rmdir(path)


if __name__ == "__main__":
	mods_dir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	
	extensions_to_remove = (
		".class", ".txt", ".TXT", ".properties",
		".info", ".obj", ".dat", ".ogg",
		".MF", ".java", ".cfg", ".lang",
		".lua", ".img", ".bin", ".tps",
		".2", ".3"
	)

	for filename in os.listdir(mods_dir):
		if filename.endswith((".zip", ".jar")):
			file_path = os.path.join(mods_dir, filename)
			# print(file_path)
			with zipfile.ZipFile(file_path, 'r') as zip_ref:
				zip_ref.extractall(mods_dir)
			os.remove(file_path)

	for root, subdirs, files in os.walk(mods_dir):
		for filename in files:
			file_path = os.path.join(root, filename)
			_, extension = os.path.splitext(filename)
			
			if filename.endswith(extensions_to_remove) or extension == "":
				# print(file_path)
				os.remove(file_path)
			else:
				if not filename.endswith(".png"):
					print("File that isn't .png:", file_path)

	remove_empty_folders(mods_dir, remove_root=False)