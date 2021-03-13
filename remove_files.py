import os


def removeEmptyFolders(path, removeRoot=True):
  'Function to remove empty folders'
  if not os.path.isdir(path):
    return

  # remove empty subfolders
  files = os.listdir(path)
  if len(files):
    for f in files:
      fullpath = os.path.join(path, f)
      if os.path.isdir(fullpath):
        removeEmptyFolders(fullpath)

  # if folder empty, delete it
  files = os.listdir(path)
  if len(files) == 0 and removeRoot:
    print("Removing empty folder:", path)
    os.rmdir(path)


if __name__ == "__main__":
    modsDir = "mods" # Watch out with this path, you can accidentally delete everything on your computer with it!
    removeFilesWithExtension = (".class", ".txt", ".TXT")

    for root, subdirs, files in os.walk(modsDir):
        for filename in files:
            if filename.endswith(removeFilesWithExtension):
                filePath = os.path.join(root, filename) 
                # print(filePath)
                os.remove(filePath)

    removeEmptyFolders(modsDir, removeRoot=False)