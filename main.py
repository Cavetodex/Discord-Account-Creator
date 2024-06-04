import subprocess
import os

def execute_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen von {script_path}: {e}")

def main():
    script_directory = os.path.join(os.path.dirname(__file__), 'source')
    stub_name = 'stub.py'
    adapter_name = 'adapter.py'
    capsolver_name = 'capsolver.py'
    stub_path = os.path.join(script_directory, stub_name)
    adapter_path = os.path.join(script_directory, adapter_name)
    capsolver_path = os.path.join(script_directory, capsolver_name)

    # Execute all scripts in parallel
    subprocess.Popen(['python', stub_path])
    subprocess.Popen(['python', adapter_path])
    subprocess.Popen(['python', capsolver_path])

if __name__ == "__main__":
    main()
