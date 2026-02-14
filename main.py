from scanner import scan_folder

def view_logs():
    try:
        with open("scan_log.txt", "r") as log:
            print("\n--- Scan Logs ---")
            print(log.read())
    except FileNotFoundError:
        print("No logs found yet.")

def main():
    while True:
        print("\n====== BASIC ANTIVIRUS ======")
        print("1. Scan Folder")
        print("2. View Logs")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            scan_folder("test_files")
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Exiting Antivirus...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()