import os
import shutil

from_dir = "C:/Users/Dev/Downloads/files"
to_dir = "C:/Users/Dev/Document/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.doc', '.docx', '.pdf', '.ppt', '.pptx', '.txt']:
         path1 = "C:/Users/Dev/Downloads/files" + '/' + file_name
         path2 = "C:/Users/Dev/Document/Document_Files"
         path3 = "C:/Users/Dev/Document/Document_Files" + '/' + file_name

         if os.path.exists(path2):
             print("Moving" + file_name + ".....")
             shutil.move(path1, path3)
         else:
             os.makedirs(path2)
             print("Moving" + file_name + ".....")
             shutil.move(path1, path3)

