import subprocess
import sys
import os

# Function to create a virtual environment
def create_virtualenv(env_name):
    subprocess.run([sys.executable, '-m', 'venv', env_name])

# Function to install packages from requirements.txt
def install_requirements(env_name):
    subprocess.run([os.path.join(env_name, 'Scripts' if os.name == 'nt' else 'bin', 'pip'), 'install', '-r', 'requirements.txt'])

def main():
    # Name of the virtual environment
    env_name = 'myenv'

    # Create virtual environment
    print(f"Creating virtual environment: {env_name}")
    create_virtualenv(env_name)

    # Install packages
    print("Installing packages from requirements.txt")
    install_requirements(env_name)

    print("Setup complete!")

if __name__ == "__main__":
    main()
