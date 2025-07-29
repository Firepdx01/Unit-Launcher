# version.py
import minecraft_launcher_lib
from minecraft_launcher_lib.utils import get_minecraft_directory, get_installed_versions

def show_installed_versions():
    mc_dir = get_minecraft_directory()
    installed = get_installed_versions(mc_dir)
    return [ver["id"] for ver in installed]

if __name__ == "__main__":
    versions = show_installed_versions()
    print("Installed Versions:")
    for v in versions:
        print(v)
