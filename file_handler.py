import os
import shutil
from datetime import datetime

def copy_files(input_dir, output_dir):
    # Dictionary to hold files grouped by their edit date
    files_by_date = {}
    # List to hold the paths of new copied files
    new_files = []
    
    try:
        # Step 1: List all files in the input directory
        for filename in os.listdir(input_dir):
            source = os.path.join(input_dir, filename)
            
            # Step 2: Fetch the modification time
            mod_time = os.path.getmtime(source)
            
            # Step 3: Convert to YYYYMMDD format
            mod_date_str = datetime.fromtimestamp(mod_time).strftime('%Y%m%d')
            
            # Step 4: Add to dictionary
            if mod_date_str not in files_by_date:
                files_by_date[mod_date_str] = []
            files_by_date[mod_date_str].append(source)

        # Step 5: Create directories and copy files
        for mod_date_str, files in files_by_date.items():
            target_dir = os.path.join(output_dir, mod_date_str)
            os.makedirs(target_dir, exist_ok=True)
            for source in files:
                if source.endswith("WAV"):
                    filename = os.path.basename(source)
                    base_name, _ = os.path.splitext(filename)
        
                    # Create a new filename with the same base name but with a .txt extension
                    txt_filename = f"{base_name}.txt"
        
                    # Create the full path for the target .txt file
                    txt_target = os.path.join(target_dir, txt_filename)
        
                    # Check if a .txt file with the same base name already exists
                    if not os.path.exists(txt_target):
                        new_files.append((source,txt_target))
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    return new_files
