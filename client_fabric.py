# client_fabric.py
import minecraft_launcher_lib
from minecraft_launcher_lib.fabric import install_fabric
from minecraft_launcher_lib.utils import get_minecraft_directory

def install_fabric_client(client_version, mc_dir=None, callback=None):
    if not mc_dir:
        mc_dir = get_minecraft_directory()
    try:
        return install_fabric(client_version, mc_dir, callback=callback)
    except Exception as e:
        print(f"Error installing Fabric: {e}")
        return None

if __name__ == "__main__":
    version = input("Enter Minecraft version for Fabric installation: ")
    result = install_fabric_client(version)
    if result:
        print("Fabric installed successfully, new version id:", result)
