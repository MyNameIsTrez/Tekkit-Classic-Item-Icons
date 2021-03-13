import os, zipfile


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
	
	removeFilesWithExtension = (
		".class", ".txt", ".TXT", ".properties",
		".info", ".obj", ".dat", ".ogg",
		".MF", ".java", ".cfg", ".lang",
		".lua", ".img", ".bin", ".tps",
		".2", ".3"
	)

	for filename in os.listdir(modsDir):
		if filename.endswith((".zip", ".jar")):
			filePath = os.path.join(modsDir, filename)
			# print(filePath)
			with zipfile.ZipFile(filePath, 'r') as zip_ref:
				zip_ref.extractall(modsDir)
			os.remove(filePath)

	for root, subdirs, files in os.walk(modsDir):
		for filename in files:
			filePath = os.path.join(root, filename)
			_, extension = os.path.splitext(filename)
			
			if filename.endswith(removeFilesWithExtension) or extension == "":
				# print(filePath)
				os.remove(filePath)
			else:
				if not filename.endswith(".png"):
					print("File that isn't .png:", filePath)

	removeEmptyFolders(modsDir, removeRoot=False)