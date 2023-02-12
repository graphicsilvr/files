import os
import zipfile
import shutil

def clean_cache():
    cache_dir = "cache"
    if os.path.exists(cache_dir):
        print("The following files will be deleted:")
        print(os.listdir(cache_dir))
        for filename in os.listdir(cache_dir):
            file_path = os.path.join(cache_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print("Failed to delete file:", file_path)
                print("Error:", e)
        print("Cache folder has been deleted.")
    else:
        print("Cache folder does not exist.")
        os.mkdir(cache_dir)
        print("Cache folder has been created.")

def cache_zip(zip_file_path: str, cache_dir: str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)

def cached_files():
    cache_dir = "cache"
    files = []
    for r, d, f in os.walk(cache_dir):
        for file in f:
            files.append(os.path.abspath(os.path.join(r, file)))
    return files

def find_password(files):
    password = "default"
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            if "password" in content:
                password = content.split("password:")[1].strip()
                break
    return password

if __name__ == "__main__":
    clean_cache()
    cache_zip("data.zip", "cache")
    files = cached_files()
    password = find_password(files)
    if password != "default":
        print(f"Password found: {password}")
    else:
        print("Password not found.")
