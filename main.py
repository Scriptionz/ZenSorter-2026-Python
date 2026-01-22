# Scripted by @Emir Karadağ v14.8 [2026-2027]
# GitHub: @Scriptionz [https://github.com/Scriptionz] 
# LinkedIn: @Emir Karadağ [https://www.linkedin.com/in/emir-karadağ-617a013a2/]

# !! Licensed under the MIT License. !!

import os
import shutil
import time
import sys
from datetime import datetime

# --------------- CONFIGURATION LAYER (Tuning Panel) ----------------- #

# TARGET DIRECTORY PATH
# Standard: os.path.join(os.path.expanduser("~"), "Desktop")
# Manual Example: TARGET_PATH = "C:/Users/Name/Downloads"
TARGET_PATH = os.path.join(os.path.expanduser("~"), "Pictures")

# FILE CATEGORIES MAPPING
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".ico"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".md"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Programming": [".py", ".js", ".cpp", ".html", ".css", ".java", ".json", ".sh"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Executables": [".exe", ".msi", ".dmg"]
}

# GLOBAL SYSTEM SETTINGS
SETTINGS = {
    "ask_confirmation": True,       # Require user approval before execution
    "create_report": True,          # Generate a summary .txt file
    "case_sensitive": False,        # Treat .JPG and .jpg as the same
    "verbose_mode": True,           # Print real-time move status
    "auto_rename_duplicates": True  # If file exists, rename instead of skipping
}

# ----------------- SYSTEM LOGIC ----------------- #

def get_unique_path(path):
    """Generates a unique filename if a duplicate exists in the target folder."""
    if not os.path.exists(path):
        return path
    
    filename, extension = os.path.splitext(path)
    timestamp = datetime.now().strftime("%H%M%S")
    return f"{filename}_{timestamp}{extension}"

def organize_files():
    """Scans the directory and sorts files into categorized folders."""
    
    # 1. Path Validation
    if not os.path.exists(TARGET_PATH):
        print(f"\n[!] ERROR: Target path not found: {TARGET_PATH}")
        return 0

    # 2. Safety Confirmation
    if SETTINGS["ask_confirmation"]:
        print("\n" + "="*50)
        print(f"ZEN SORTER | SYSTEM READY")
        print(f"TARGET: {TARGET_PATH}")
        print("="*50)
        confirm = input("Proceed with organization? (y/n): ").lower().strip()
        if confirm not in ['yes', 'y']:
            print("\n[CANCELLED] Operation aborted by user.")
            return -1

    moved_count = 0
    report_data = []
    
    # 3. Processing Loop
    for item in os.listdir(TARGET_PATH):
        source_path = os.path.join(TARGET_PATH, item)

        # Skip directories and hidden system files
        if os.path.isdir(source_path) or item.startswith("."):
            continue

        # Identify Extension
        _, extension = os.path.splitext(item)
        search_ext = extension if SETTINGS["case_sensitive"] else extension.lower()

        # Find Matching Category
        category_name = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if search_ext in extensions:
                category_name = category
                break

        # Prepare Destination
        dest_dir = os.path.join(TARGET_PATH, category_name)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        dest_path = os.path.join(dest_dir, item)
        
        # Handle Duplicates
        if SETTINGS["auto_rename_duplicates"]:
            dest_path = get_unique_path(dest_path)

        # Execution
        try:
            shutil.move(source_path, dest_path)
            moved_count += 1
            log_entry = f"[{datetime.now().strftime('%H:%M:%S')}] {item} -> {category_name}/"
            report_data.append(log_entry)
            
            if SETTINGS["verbose_mode"]:
                print(f"[SUCCESS] {log_entry}")
        except Exception as e:
            print(f"[FAILED] Could not move {item}: {e}")

    # 4. Report Generation
    if SETTINGS["create_report"] and report_data:
        report_file = os.path.join(TARGET_PATH, "ZenSorter_Summary.txt")
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(f"ZenSorter Execution Report\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source: {TARGET_PATH}\n")
            f.write("-" * 40 + "\n")
            f.write("\n".join(report_data))
        print(f"\n[INFO] Summary report generated at: {report_file}")

    return moved_count

if __name__ == "__main__":
    start_time = time.time()
    result = organize_files()
    
    if result > 0:
        elapsed = round(time.time() - start_time, 2)
        print(f"\nCOMPLETED: {result} files organized in {elapsed}s.")
        print("Desktop is now optimized. ✨")
    elif result == 0:
        print("\nIDLE: No eligible files found to organize.")
