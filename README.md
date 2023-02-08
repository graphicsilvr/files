# files

Introduction
This code implements functionality for caching, extracting and searching for a password in a zip file. The code consists of several functions as described below:

clean_cache(): Cleans up the existing cache folder. If the folder does not exist, it will create one.
cache_zip(zip_file_path, cache_dir): Extracts the contents of a zip file to the cache folder.
cached_files(): Returns a list of files present in the cache folder.
find_password(files): Searches for the password in the list of files.
Requirements
The following packages must be installed to run the code:

os: Provides a way of using operating system dependent functionality.
zipfile: Used to extract files from a zip file.
shutil: Provides a higher level interface to file operations.
Usage
To run the code, simply execute it as a python script. The code will perform the following steps:

Clean the cache folder.
Extract the contents of data.zip to the cache folder.
Get the list of files present in the cache folder.
Search for the password in the list of files.
If the password is found, print it to the console.
Output
The code will output the following:

If the cache folder does not exist, it will create one and display a message "Cache folder has been created."
If the cache folder exists, it will display the list of files that will be deleted and a message "Cache folder has been deleted."
If the password is found, it will display "Password found: <password>".
If the password is not found, it will display "Password not found."
Limitations
The code assumes the existence of a zip file named data.zip. If the file does not exist, the code will raise a FileNotFoundError.
The code assumes the presence of the word "password" in the file to search for the password. If the password is stored differently, the code will not find it.
