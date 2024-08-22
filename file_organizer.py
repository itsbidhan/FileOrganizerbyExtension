import os
import shutil
from datetime import datetime

def create_directory(directory):
    """
    Create a directory if it doesn't exist.
    
    Args:
    directory (str): Path of the directory to be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_extension(filename):
    """
    Get the file extension from a filename.
    
    Args:
    filename (str): Name of the file.
    
    Returns:
    str: The file extension (lowercase) or 'no_extension' if there's no extension.
    """
    return os.path.splitext(filename)[1][1:].lower() or 'no_extension'

def organize_files(source_dir, dest_dir):
    """
    Organize files from the source directory into subdirectories in the destination directory based on their extensions.
    
    Args:
    source_dir (str): Path of the source directory containing files to organize.
    dest_dir (str): Path of the destination directory where organized files will be moved.
    """
    create_directory(dest_dir)
    
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_ext = get_extension(filename)
            dest_subdir = os.path.join(dest_dir, file_ext)
            create_directory(dest_subdir)
            
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_subdir, filename)
            
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename} -> {dest_subdir}")

def main():
    """
    Main function to run the file organizer.
    """
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")
    
    if not os.path.exists(source_directory):
        print("Error: Source directory does not exist.")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_directory = os.path.join(destination_directory, f"organized_{timestamp}")
    
    organize_files(source_directory, destination_directory)
    print(f"File organization complete. Organized files are in: {destination_directory}")

if __name__ == "__main__":
    main()