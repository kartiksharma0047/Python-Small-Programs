import os
from pathlib import Path
import string
import psutil

# Get all drive letters (C:/, D:/, E:/, etc.)
def get_target_folder():
    desktop = Path.home() / "Desktop"
    target = Path(r"C:\Users\karti\OneDrive\Desktop\Python Codes")
    return target if target.exists() else None

# Search all drives for matching folder names
def find_folders_system_wide(folder_name):
    target_folder = get_target_folder()
    matching_folders = []

    if target_folder is None:
        print("The 'Python Codes' folder does not exist on Desktop.")
        return matching_folders

    try:
        for path in target_folder.rglob('*'):
            if path.is_dir() and path.name.lower() == folder_name.lower():
                matching_folders.append(path)

        # If no matching folders found, list all folders
        if not matching_folders:
            print(f"\nNo folders named '{folder_name}' found.")
            print("Showing all folders in 'Python Codes':")
            for path in target_folder.rglob('*'):
                if path.is_dir():
                    matching_folders.append(path)

    except PermissionError:
        pass  # skip protected folders

    return matching_folders

def show_folders(self):
    if not self.folder_paths:
        print("\nNo folders found in 'Python Codes' at all.")
        return False
    else:
        print("\nAvailable folders:")
        for idx, path in enumerate(self.folder_paths, start=1):
            print(f"[{idx}] {path}")
        return True

# Main Clutter Cleaning Class
class ClearClutter:
    def __init__(self, folder):
        self.folder_name = folder
        self.folder_paths = find_folders_system_wide(folder)

    def show_folders(self):
        if not self.folder_paths:
            print(f"\nNo folders found with the name '{self.folder_name}'.")
            return False
        else:
            print("\nFound folders:")
            for idx, path in enumerate(self.folder_paths, start=1):
                print(f"[{idx}] {path}")
            return True

    def select_folder(self):
        try:
            choice = int(input("\nSelect a folder by number: "))
            selected = self.folder_paths[choice - 1]
            if any(selected.iterdir()):
                return selected
            else:
                print(f"\n'{selected}' is empty. Choose another or return to menu.")
                return None
        except (IndexError, ValueError):
            print("Invalid selection!")
            return None

    def rename_items(self, folder_path):
        items = list(folder_path.iterdir())
        if not items:
            print("Folder is empty.")
            return

        while True:
            print("""
Choose Renaming Style:
[1] Numeric (1.png, 2.txt)
[2] Alphabetic [lowercase] (a.png, b.txt)
[3] Alphabetic [UPPERCASE] (A.png, B.txt)
[4] Default Name (you'll enter the base name)
[5] Previous Step
""")
            option = input("Enter your choice: ")

            if option == '1':
                self.rename_numeric(items, folder_path)
                break
            elif option == '2':
                self.rename_alphabetic(items, folder_path, lowercase=True)
                break
            elif option == '3':
                self.rename_alphabetic(items, folder_path, lowercase=False)
                break
            elif option == '4':
                base = input("Enter the base name for files: ")
                self.rename_default(items, folder_path, base)
                break
            elif option == '5':
                return
            else:
                print("Invalid option! Try again.")

    def rename_numeric(self, items, folder_path):
        counter = 1
        for item in items:
            ext = item.suffix if item.is_file() else ""
            new_name = f"{counter}{ext}" if ext else f"{counter} (Folder)"
            new_path = folder_path / new_name
            try:
                item.rename(new_path)
                print(f"Renamed '{item.name}' to '{new_name}'")
                counter += 1
            except Exception as e:
                print(f"Error renaming '{item.name}': {e}")

    def rename_alphabetic(self, items, folder_path, lowercase=True):
        letters = string.ascii_lowercase if lowercase else string.ascii_uppercase
        counter = 0
        for item in items:
            if counter >= len(letters):
                print("Limit reached! Too many files for alphabetic renaming.")
                break
            ext = item.suffix if item.is_file() else ""
            new_name = f"{letters[counter]}{ext}" if ext else f"{letters[counter]} (Folder)"
            new_path = folder_path / new_name
            try:
                item.rename(new_path)
                print(f"Renamed '{item.name}' to '{new_name}'")
                counter += 1
            except Exception as e:
                print(f"Error renaming '{item.name}': {e}")

    def rename_default(self, items, folder_path, base):
        counter = 1
        for item in items:
            ext = item.suffix if item.is_file() else ""
            new_name = f"{base}({counter}){ext}" if ext else f"{base}({counter}) (Folder)"
            new_path = folder_path / new_name
            try:
                item.rename(new_path)
                print(f"Renamed '{item.name}' to '{new_name}'")
                counter += 1
            except Exception as e:
                print(f"Error renaming '{item.name}': {e}")

# Main Menu
def main_menu():
    while True:
        print("""
Folder Clutter Cleaner (Remeber Path of the folder should be like this - "C:\Users\karti\OneDrive\Desktop\Python Codes" Only folder inside this path will be searched for)
[1] Start Program
[2] Exit
""")
        user_input = input("Enter your choice: ")

        if user_input == '1':
            folder_name = input("Enter folder name to search for: ")
            clutter = ClearClutter(folder_name)

            if not clutter.show_folders():
                continue

            while True:
                selected_folder = clutter.select_folder()
                if selected_folder:
                    clutter.rename_items(selected_folder)
                    break
                else:
                    choice = input("\nDo you want to choose another folder? (y/n): ").lower()
                    if choice != 'y':
                        break

        elif user_input == '2':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please select 1 or 2.")

if __name__ == "__main__":
    main_menu()
