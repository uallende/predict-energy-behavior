import subprocess
import os
import zipfile

def download_kaggle_data(competition_name):
    subprocess.run(["kaggle", "competitions", "download", "-c", competition_name, "-p", competition_name], check=True)
    
    zip_path = os.path.join(competition_name, f"{competition_name}.zip")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(competition_name)

def update_gitignore(dest_folder, zip_name):
    with open(".gitignore", "a") as f:
        f.write(f"{dest_folder}/*\n")  # Ignore all files in the destination folder
        f.write(f"{zip_name}\n") 
        f.write(f"data/\n") # Ignore the ZIP file itself

if __name__ == "__main__":
    competition_name = "predict-energy-behavior-of-prosumers"
    
    # Check if Kaggle API key exists
    kaggle_path = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_path):
        print("Kaggle API key not found. Please make sure kaggle.json is placed in ~/.kaggle/")
    else:
        download_kaggle_data(competition_name)
        zip_name = f"{competition_name}.zip"
        update_gitignore(competition_name, zip_name)