import os
import time



def get_tracked_files():
    tracked_files = {}
    tracking_file = os.path.join(os.getcwd(), ".veta", "tracking.txt")
    with open(tracking_file, 'r') as tracking_file:
        for line in tracking_file:
            file_name, timestamp = line.strip().split(',')
            tracked_files[file_name] = float(timestamp)

    return tracked_files
def status():
    tracked_files = get_tracked_files()  
    untracked_files = []
    modified_files = []

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if not file.startswith('.') and ( root.find("/.") == -1):  # Exclude hidden files
                file_path = os.path.relpath(os.path.join(root, file), os.getcwd())
                if file_path in tracked_files:
                    last_updated_time = os.path.getmtime(file_path)
                    if last_updated_time > tracked_files[file_path]:
                        modified_files.append(file_path)
                else:
                    untracked_files.append(file_path)

    print("Modified files:")
    for file in modified_files:
        print(file)

    print("Untracked files:")
    for file in untracked_files:
        print(file)