# startfile.py
import subprocess
import os

import sys

def ensure_data_dirs():
    if not os.path.exists("data"):
        os.mkdir("data")
    vectordb_path = os.path.join("data", "vectordb")
    if not os.path.exists(vectordb_path):
        os.mkdir(vectordb_path)


def run_script(script_path):
    print(f"Running {script_path} ...")
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_path}:\n{e}")
        exit(1)

def main():
    ensure_data_dirs()
    run_script("src/prepare_sqldb.py")
    run_script("src/prepare_vectordb.py")
    run_script("src/chat_in_ui.py")

if __name__ == "__main__":
    main()
