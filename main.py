import subprocess
import os

def main():
    script_directory = os.path.join(os.path.dirname(__file__), 'source')
    script_names = ['stub.py', 'adapter.py', 'anti.py']

    for script_name in script_names:
        script_path = os.path.join(script_directory, script_name)
        subprocess.Popen(['python', script_path])

if __name__ == "__main__":
    main()
