import os


def removeEmptyFolders(path, removeRoot=True):
	if not os.path.isdir(path):
		return

	# Remove empty subfolders.
	files = os.listdir(path)
	if len(files):
		for f in files:
			fullpath = os.path.join(path, f)
			if os.path.isdir(fullpath):
				removeEmptyFolders(fullpath)

	# If the folder is empty, remove it.
	files = os.listdir(path)
	if len(files) == 0 and removeRoot:
		print("Removing empty folder:", path)
		os.rmdir(path)


if __name__ == "__main__":
	modsDir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
	removeFilesWithExtension = (".class", ".txt", ".TXT", ".properties", ".info", ".obj", ".dat", ".ogg", ".MF", ".java", ".cfg", ".lang", ".lua", ".")

	for root, subdirs, files in os.walk(modsDir):
		for filename in files:
			filePath = os.path.join(root, filename) 
			if filename.endswith(removeFilesWithExtension):
				# print(filePath)
				os.remove(filePath)
			else:
				if not filename.endswith(".png"):
					print("File that isn't .png:", filePath)

	removeEmptyFolders(modsDir, removeRoot=False)