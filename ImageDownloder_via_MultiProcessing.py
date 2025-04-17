import multiprocessing
import requests
import os
import shutil

image_urls = [
    "https://picsum.photos/id/237/300/200",
    "https://picsum.photos/id/238/300/200",
    "https://picsum.photos/id/239/300/200",
    "https://picsum.photos/id/240/300/200",
    "https://picsum.photos/id/241/300/200",
    "https://picsum.photos/id/242/300/200",
    "https://picsum.photos/id/243/300/200",
    "https://picsum.photos/id/244/300/200",
    "https://picsum.photos/id/245/300/200",
    "https://picsum.photos/id/246/300/200"
]

IMAGE_FOLDER = "Images"

def ensure_folder():
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

def download_file(url, name):
    try:
        print(f"Started Downloading {name} from {url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f"{IMAGE_FOLDER}/{name}.jpg", "wb") as f:
                f.write(response.content)
            print(f"Finished Downloading {name}")
        else:
            print(f"Failed to download {name}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

def download_demo_images():
    ensure_folder()
    processes = []
    for index, url in enumerate(image_urls):
        p = multiprocessing.Process(target=download_file, args=(url, f"DemoImage_{index}"))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def empty_folder():
    ensure_folder()
    files = os.listdir(IMAGE_FOLDER)
    if not files:
        print("The folder is already empty.")
        return

    print("Files present in the folder:")
    for file in files:
        print(f"- {file}")

    confirm = input("Do you want to delete all these files? (yes/no): ").strip().lower()
    if confirm == 'yes':
        for file in files:
            os.remove(os.path.join(IMAGE_FOLDER, file))
        print("All files have been deleted.")
    else:
        print("Deletion cancelled.")

def custom_download_images():
    ensure_folder()
    try:
        count = int(input("Enter the number of images you want to download: "))
        if count <= 0:
            print("Number must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    processes = []
    for i in range(count):
        while True:
            url = input(f"Enter URL for image {i + 1}: ").strip()
            if url:
                break
            else:
                print("URL cannot be empty. Please enter a valid URL.")

        p = multiprocessing.Process(target=download_file, args=(url, f"CustomImage_{i}"))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def start_program():
    while True:
        print("\n(1) Download Images")
        print("(2) Empty Folder")
        print("(3) Demo Images")
        option = input("Enter your choice: ").strip()

        if option == "1":
            custom_download_images()
        elif option == "2":
            empty_folder()
        elif option == "3":
            download_demo_images()
        else:
            print("Invalid choice, please select a valid option (1/2/3).")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("(1) Start Program")
        print("(2) Exit Program")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            start_program()
        elif choice == "2":
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid input, please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()
