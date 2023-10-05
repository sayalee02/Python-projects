import os
import shutil

def organize_files(source_dir):
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = filename.split('.')[-1]
            target_dir = os.path.join(source_dir, file_extension)
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)
            
            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {target_dir}")

source_directory = "C:\\Users\\LENOVO\\Desktop\\Python Internship\\Level 3\\task3(folder)"
organize_files(source_directory)
