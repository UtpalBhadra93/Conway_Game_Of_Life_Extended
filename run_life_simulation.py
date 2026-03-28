# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

import os
import sys
import subprocess
import platform

ENV_NAME = "life_env"

def is_venv_existing():
    return os.path.exists(ENV_NAME)

def run_command(cmd_list):
    """Run a system command and print output in real-time."""
    process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end="")
    process.wait()
    if process.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd_list)}")

def create_virtualenv():
    print("Creating virtual environment...")
    run_command([sys.executable, "-m", "venv", ENV_NAME])

def install_dependencies():
    print("Installing dependencies (numpy, pygame)...")
    pip_path = os.path.join(ENV_NAME, "Scripts" if platform.system() == "Windows" else "bin", "pip")
    run_command([pip_path, "install", "--upgrade", "pip"])
    run_command([pip_path, "install", "numpy", "pygame"])

def run_main():
    print("Launching main.py...")
    python_path = os.path.join(ENV_NAME, "Scripts" if platform.system() == "Windows" else "bin", "python")
    run_command([python_path, "main.py"])

if __name__ == "__main__":
    try:
        if not is_venv_existing():
            create_virtualenv()
            install_dependencies()
        else:
            print(f"Virtual environment '{ENV_NAME}' already exists. Skipping creation.")
        run_main()
    except Exception as e:
        print(f"Error: {e}")
