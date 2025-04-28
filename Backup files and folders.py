import os
import argparse
from datetime import datetime
import shutil

exclude_folders_files = [".*", ".git", ".svn", "desktop.ini", "Personal Vault.lnk"]

# Add option parameters and read the input
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="Source path",type=str)
parser.add_argument("-d", "--destination", help="Destination path", type=str)
args = parser.parse_args()
source = str(args.source)
destination = str(args.destination)

# Check for the source
while True:
    if not os.path.exists(source):
        source = input("What would you like to backup? Provide the path: ")

        if os.path.exists(source):
            break
    else:
        break

# Check for the destination
while True:
    if not os.path.exists(destination):
        drives = os.popen("fsutil fsinfo drives").readlines()

        print("Available drives:")
        for drive in list(drives):
            print(drive.strip())

        print("")
        destination = input("Where do you want to store the backup? Provide the path: ")
        
        if os.path.exists(destination):
            break
    else:
        break

date_today = datetime.now()
date_folder = date_today.strftime("%Y-%m-%d")

destination_full = os.path.join(destination, date_folder)

print(f"Backup '{source}' to '{destination_full}'")
shutil.copytree(source, destination_full, dirs_exist_ok = True, ignore=shutil.ignore_patterns(*exclude_folders_files))

print("Don't forget to make an export from your vault!")