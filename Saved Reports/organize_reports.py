import os
import shutil

# Define the working directory (test directory)
working_dir = "PA1"

# Process each file in the working directory
for file in os.listdir(working_dir):
    # Look for main HTML files starting with "Matches"
    if file.endswith(".html") and file.startswith("Matches"):
        # Extract the student CruzID from the file name
        parts = file.split("_")
        cruz_id = parts[2] if len(parts) > 2 else "unknown"

        # Create a folder for the CruzID if it doesn't already exist
        student_folder = os.path.join(working_dir, cruz_id)
        os.makedirs(student_folder, exist_ok=True)

        # Move the main HTML file to the student's folder
        src_html_path = os.path.join(working_dir, file)
        dest_html_path = os.path.join(student_folder, file)
        shutil.move(src_html_path, dest_html_path)

        # Look for the companion folder (same name as the main file, minus ".html")
        companion_folder_name = file.replace(".html", "_files")
        companion_folder_path = os.path.join(working_dir, companion_folder_name)
        if os.path.exists(companion_folder_path):
            # Move the companion folder to the student's folder
            dest_companion_folder_path = os.path.join(student_folder, companion_folder_name)
            shutil.move(companion_folder_path, dest_companion_folder_path)

        print(f"Organized {file} and its companion folder into {student_folder}")

