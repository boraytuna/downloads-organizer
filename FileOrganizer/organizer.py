import os
import shutil
import time

# Define paths
downloads_dir = '/Users/boraytuna/Downloads'

# Ensure target directories exist
subdirectories = ["/Images", "/Music", "/Videos", "/Documents", "/Code", "/Other"]
for subdir in subdirectories:
    os.makedirs(downloads_dir + subdir, exist_ok=True)

# File extension categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
music_extensions = ['.mp3', ".wav", ".aiff"]
video_extensions = [".mp4"]
doc_extensions = [".txt", ".pdf", ".docx", ".doc"]
code_extensions = [".py", ".java", ".js", ".cpp", ".c", ".cs", ".swift", ".html", ".css", ".lua"]

def has_code_files(dir_path):
    """Check if a directory contains code files."""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if any(file.endswith(ext) for ext in code_extensions):
                return True
    return False

while True:
    # Organize Downloads folder
    for item in os.listdir(downloads_dir):
        item_path = os.path.join(downloads_dir, item)

        if os.path.isfile(item_path):
            extension = os.path.splitext(item)[1].lower()
            if extension in image_extensions:
                target = os.path.join(downloads_dir, "Images")
            elif extension in music_extensions:
                target = os.path.join(downloads_dir, "Music")
            elif extension in video_extensions:
                target = os.path.join(downloads_dir, "Videos")
            elif extension in doc_extensions:
                target = os.path.join(downloads_dir, "Documents")
            elif extension in code_extensions:
                target = os.path.join(downloads_dir, "Code")
            else:
                target = os.path.join(downloads_dir, "Other")
            shutil.move(item_path, os.path.join(target, item))
        elif os.path.isdir(item_path) and item not in [subdir.strip("/") for subdir in subdirectories]:
            # If the directory contains code files, move it to the "Code" folder
            if has_code_files(item_path):
                shutil.move(item_path, os.path.join(downloads_dir, "Code", item))
            else:
                shutil.move(item_path, os.path.join(downloads_dir, "Other", item))

    time.sleep(60)  # Check every 60 seconds
