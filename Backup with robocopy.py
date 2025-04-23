import os
import sys
from datetime import datetime

# Function to check if a path exists
def check_path_exist(path_name):
    if os.path.exists(path_name):
        return True
    else:
        return False

# Check if argument 1 was provided
if len(sys.argv) >= 2:
    source = sys.argv[1]
else:
    source = ""

# Check if argument 2 was provided
if len(sys.argv) >= 3:
    destination = sys.argv[2]
else:
    destination = ""

# While loop to check for the source
while True:
    if check_path_exist(source) == False:
        source = input("What would you like to backup? Provide the path: ")

        if check_path_exist(source) == True:
            break
    else:
        break

# While loop to check for the destination
while True:
    if check_path_exist(destination) == False:
        drives = os.popen("fsutil fsinfo drives").readlines()

        for drive in list(drives):
            print(drive.strip())

        print("")
        destination = input("Where do you want to store the backup? Provide the path: ")
        
        if check_path_exist(destination) == True:
            break
    else:
        break

date_today = datetime.now()
date_folder = date_today.strftime("%Y-%m-%d")

destination_date = f"{destination}\\{date_folder}"
options = "/E /R:0 /MIR /A-:SH /XD '.git' '.svn' /XF 'desktop.ini' 'Personal Vault.lnk'"

print(f"Backup '{source}' to '{destination_date}'")
os.system(f"robocopy {source} {destination_date} {options}")