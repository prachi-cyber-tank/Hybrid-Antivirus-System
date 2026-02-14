import os
from hash_utils import calculate_hash
from quarantine import move_to_quarantine
from datetime import datetime


def load_signatures():
    try:
        with open("signatures.txt", "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        print("Signature database not found!")
        return set()


def log_result(filename, status):
    with open("scan_log.txt", "a") as log:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{time_now} - {filename} - {status}\n")


def heuristic_scan(file_path):
    suspicious_keywords = [
        "eval(",
        "exec(",
        "os.system",
        "subprocess",
        "powershell",
        "cmd.exe"
    ]

    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read()
            for keyword in suspicious_keywords:
                if keyword in content:
                    return True
    except:
        pass

    return False


def scan_folder(folder_path):
    signatures = load_signatures()

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    print("\nScanning Started...\n")

    allowed_extensions = (".py", ".exe", ".txt", ".bat")

    infected_count = 0
    clean_count = 0
    suspicious_count = 0
    total_files = 0

    for filename in os.listdir(folder_path):
        if not filename.endswith(allowed_extensions):
            continue

        total_files += 1
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_hash = calculate_hash(file_path)

            if file_hash in signatures:
                print(f"[INFECTED - SIGNATURE] {filename}")
                log_result(filename, "INFECTED (Signature)")
                move_to_quarantine(file_path)
                infected_count += 1

            elif heuristic_scan(file_path):
                print(f"[SUSPICIOUS - HEURISTIC] {filename}")
                log_result(filename, "SUSPICIOUS (Heuristic)")
                move_to_quarantine(file_path)
                suspicious_count += 1

            else:
                print(f"[CLEAN] {filename}")
                log_result(filename, "CLEAN")
                clean_count += 1

    print("\n========== Scan Summary ==========")
    print(f"Total Files Scanned: {total_files}")
    print(f"Infected (Signature): {infected_count}")
    print(f"Suspicious (Heuristic): {suspicious_count}")
    print(f"Clean: {clean_count}")
    print("==================================")
    print("\nScan Completed.\n")