import os
import sys
from datetime import datetime

if len(sys.argv) <= 1:
    sys.exit("No folder was provided by argument!")

source_folder_arg = sys.argv[1]

if os.path.exists(source_folder_arg):
    drives = os.popen("fsutil fsinfo drives").readlines()

    for drive in list(drives):
        print(drive)

    drive_chosen = input("On what drive would you like to store the backup?")

    if os.path.exists(drive_chosen):
        date_today = datetime.now()
        date_folder = date_today.strftime("%Y-%m-%d")

        source = source_folder_arg
        destination = f"{drive_chosen}\\Backup\\{date_folder}"
        options = "/E /R:0 /MIR /A-:SH /XD '.git' '.svn' /XF 'desktop.ini' 'Personal Vault.lnk'"

        print(f"Backup '{source}' to '{destination}'")
        os.system(f"robocopy {source} {destination} {options}")
    else:
        print(f"{drive_chosen} not available!")
else:
    print(f"{source_folder_arg} not available!")