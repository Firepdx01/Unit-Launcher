# client_forge.py
import minecraft_launcher_lib
from minecraft_launcher_lib.forge import install_forge_version
from minecraft_launcher_lib.utils import get_minecraft_directory

def install_forge(client_version, mc_dir=None, callback=None):
    if not mc_dir:
        mc_dir = get_minecraft_directory()
    try:
        install_forge_version(client_version, mc_dir, callback=callback)
        return True
    except Exception as e:
        print(f"Error installing Forge: {e}")
        return False

if __name__ == "__main__":
    version = input("Enter Minecraft version for Forge installation: ")
    success = install_forge(version)
    if success:
        print("Forge installed successfully.")
