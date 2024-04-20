import subprocess
import os

def execute_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen von {script_path}: {e}")

def main():
    script_directory = os.path.join(os.path.dirname(__file__), 'source')
    script_name = 'stub.py'
    script_path = os.path.join(script_directory, script_name)
    execute_script(script_path)

if __name__ == "__main__":
    main()
    l
