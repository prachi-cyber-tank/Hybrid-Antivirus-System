import os
import shutil

def move_to_quarantine(file_path):
    quarantine_folder = "quarantine"
    
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    
    filename = os.path.basename(file_path)
    destination = os.path.join(quarantine_folder, filename)
    
    shutil.move(file_path, destination)
    print(f"[QUARANTINED] {filename} moved to quarantine.")