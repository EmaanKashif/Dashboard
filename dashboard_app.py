import zipfile
import os

# Path to your zip file
zip_file_path = 'path_to_your_zip_file.zip'
extracted_folder = 'extracted_data/'

# Create the extracted folder if it doesn't exist
os.makedirs(extracted_folder, exist_ok=True)

# Extract the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# List the files in the extracted folder (optional)
print(os.listdir(extracted_folder))

