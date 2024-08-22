We import necessary modules: os for file and directory operations, shutil for moving files, and datetime for timestamping.
The create_directory() function creates a directory if it doesn't exist.
The get_extension() function extracts the file extension from a filename. If there's no extension, it returns 'no_extension'.
The organize_files() function is the core of our organizer. It iterates through files in the source directory, creates subdirectories based on file extensions in the destination directory, and moves files to their respective subdirectories.
The main() function serves as the entry point of our script. It prompts the user for source and destination directories, creates a timestamped folder in the destination directory, and calls organize_files().
We use if __name__ == "__main__": to ensure the main() function only runs when the script is executed directly.