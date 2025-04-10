from pathlib import Path

class Library:
    fileName = "LibraryStore.txt"
    file = Path(fileName)

    def __init__(self):
        if not self.file.exists():
            self.file.touch()

    def viewBooks(self):
        with self.file.open("r") as f:
            lines = f.readlines()
            if not lines:
                print("No books have been added yet.")
            else:
                print("\nBooks in Library:\n")
                for line in lines:
                    print(line.strip())
                print(f"\nTotal books: {len(lines)}")

        print("\n(1). Back to Library Menu\n(2). Add Books")
        choice = input("Choose option: ")
        if choice == '1':
            libraryAccess()
        elif choice == '2':
            self.addBooks()
        else:
            print("Invalid choice!")
            self.viewBooks()

    def addBooks(self):
        print("\n(1). Add Single Book\n(2). Add Multiple Books")
        choice = input("Choose option: ")
        with self.file.open("r") as f:
            current_lines = f.readlines()
        next_number = len(current_lines) + 1

        if choice == '1':
            book = input("Enter book name: ")
            with self.file.open("a") as f:
                f.write(f"{next_number}. {book}\n")
            print("Book added successfully.\n")

        elif choice == '2':
            try:
                count = int(input("How many books to add: "))
                booksList = []
                for i in range(count):
                    book = input(f"Enter book {i+1} name: ")
                    booksList.append(f"{next_number + i}. {book}\n")
                with self.file.open("a") as f:
                    f.writelines(booksList)
                print("Books added successfully.\n")
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
                return self.addBooks()
        else:
            print("Invalid option.")
            return self.addBooks()

        libraryAccess()

    def removeBooks(self):
        print("\n(1). Remove Single Book\n(2). Remove Multiple Books")
        choice = input("Choose option: ")
        with self.file.open("r") as f:
            lines = f.readlines()

        if not lines:
            print("No books to remove.")
            return libraryAccess()

        for line in lines:
            print(line.strip())

        if choice == '1':
            try:
                remove_line = int(input("Enter serial number of book to remove: "))
                if 1 <= remove_line <= len(lines):
                    del lines[remove_line - 1]
                    self._saveWithRenumbering(lines)
                    print("Book removed successfully.\n")
                else:
                    print("Invalid serial number.")
                    return self.removeBooks()
            except ValueError:
                print("Invalid input. Enter a number.")
                return self.removeBooks()

        elif choice == '2':
            nums = input("Enter serial numbers to remove (comma-separated): ")
            try:
                indices = sorted(
                    [int(x.strip()) - 1 for x in nums.split(",") if x.strip().isdigit()],
                    reverse=True
                )
                for i in indices:
                    if 0 <= i < len(lines):
                        del lines[i]
                self._saveWithRenumbering(lines)
                print("Books removed successfully.\n")
            except ValueError:
                print("Invalid input. Please enter valid serial numbers.")
                return self.removeBooks()
        else:
            print("Invalid choice.")
            return self.removeBooks()

        libraryAccess()

    def _saveWithRenumbering(self, lines):
        # Renumber books starting from 1 again
        updated_lines = [f"{i+1}. {line.split('. ', 1)[-1]}" for i, line in enumerate(lines)]
        with self.file.open("w") as f:
            f.writelines(updated_lines)

# Top-level program flow
def startProgram():
    print("\n Welcome to Library Management System")
    print("(1). View Library\n(2). Exit Library")
    choice = input("Select option: ")
    if choice == '1':
        libraryAccess()
    elif choice == '2':
        print("Exiting... Goodbye!")
    else:
        print("Invalid input. Try again.\n")
        startProgram()

def libraryAccess():
    lib = Library()
    print("\n Library Menu")
    print("(1). View Books\n(2). Add Books\n(3). Remove Books\n(4). Back to Main Menu")
    choice = input("Choose Option: ")

    if choice == '1':
        lib.viewBooks()
    elif choice == '2':
        lib.addBooks()
    elif choice == '3':
        lib.removeBooks()
    elif choice == '4':
        startProgram()
    else:
        print("Invalid input. Try again.\n")
        libraryAccess()

startProgram()
