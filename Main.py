import os
import shutil


def list_files():
    try:
        files = os.listdir()
        if not files:
            print("Folder is empty.")
        else:
            for file in files:
                print(file)
    except Exception as e:
        print("Error:", e)


def create_file():
    name = input("Enter file name: ")
    try:
        with open(name, "w") as f:
            pass
        print("File created successfully.")
    except Exception as e:
        print("Error:", e)


def create_folder():
    name = input("Enter folder name: ")
    try:
        os.mkdir(name)
        print("Folder created successfully.")
    except Exception as e:
        print("Error:", e)


def delete_item():
    name = input("Enter file/folder name to delete: ")
    try:
        if os.path.isdir(name):
            shutil.rmtree(name)
        elif os.path.isfile(name):
            os.remove(name)
        else:
            print("File/Folder not found.")
            return
        print("Deleted successfully.")
    except Exception as e:
        print("Error:", e)


def rename_item():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    try:
        os.rename(old_name, new_name)
        print("Renamed successfully.")
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        print("\n=== Basic File Manager ===")
        print("1. List files")
        print("2. Create file")
        print("3. Create folder")
        print("4. Delete")
        print("5. Rename")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_files()
        elif choice == "2":
            create_file()
        elif choice == "3":
            create_folder()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            rename_item()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
