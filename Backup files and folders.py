import os
import argparse
from datetime import datetime
import shutil

exclude_folders_files = [".*", "desktop.ini", "Personal Vault.lnk"]

# Add option parameters and read the input
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="Provide a valid source path")
parser.add_argument("-d", "--destination", help="Provide a valid destination path")
args = parser.parse_args()
source = str(args.source)
destination = str(args.destination)

# Check for the source
while not os.path.isdir(source):
    source = input("What would you like to backup? Provide the path: ")

# Check for the destination
while not os.path.isdir(destination):
    drives = os.popen("fsutil fsinfo drives").readlines()

    print("Available drives:")
    for drive in list(drives):
        print(drive.strip())
    print("")

    destination = input("Where do you want to store the backup? Provide the path: ")
    
date_today = datetime.now()
date_folder = date_today.strftime("%Y-%m-%d")

destination_full = os.path.join(destination, date_folder)

print(f"Backup '{source}' to '{destination_full}'")
shutil.copytree(source, destination_full, dirs_exist_ok = True, ignore=shutil.ignore_patterns(*exclude_folders_files))

print("Don't forget to make an export from your vault!")