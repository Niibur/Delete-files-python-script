import os
import time

def search_for_files(path, searched_file):
    """
    This function searches for the file with the specified name in the directory specified by the user.
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):        
        for file in filenames:
            if file == searched_file:
                files.append(os.path.join(dirpath, file))
    return files

def confirm_excluding(files):
    """
    This function allows the user to confirm whether they want to exclude the found files.
    """
    num_files = len(files)
    print(f"> Found {num_files} file(s) with the specified name.")
    if num_files == 0:
        return
    answer = input("> Do you want to exclude the files? Type 'Yes' to confirm: ")
    if answer == "Yes":
        num_excluded = 0
        for file in files:
            try:
                os.remove(file)
                num_excluded += 1
            except OSError as e:
                print(f"> Failed to exclude file {file}: {e}")
        print(f"> Excluded {num_excluded} file(s).")

print('>>> This program searches for files to delete based on their name.')
directory = input("> Which directory do you want to scan? ")
filename = input("> What is the name of the file? ")

print(f"> Scanning the directory {directory} for files with the name {filename}...")

start_time = time.time()
files = search_for_files(directory, filename)
elapsed_time = time.time() - start_time

if len(files) == 0:
    print(f"> No files with the name {filename} were found in the directory {directory}.")
else:
    confirm_excluding(files)
    
print(f"> The total execution time was {elapsed_time:.2f} seconds.")
