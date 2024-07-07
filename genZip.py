import os
import zipfile

def zip_folder(folder_path, archive_name):
  print(f"\nIn zip folder making")
  """
  Zips a folder and its contents into a ZIP archive.

  Args:
    folder_path: Path to the folder to be zipped.
    archive_name: Name of the ZIP archive to create.
  """
  with zipfile.ZipFile(archive_name, 'w') as zip_file:
    for root, directories, files in os.walk(folder_path):
      for filename in files:
        file_path = os.path.join(root, filename)
        zip_file.write(file_path, os.path.relpath(file_path, folder_path))


