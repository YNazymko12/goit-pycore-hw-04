import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def display_directory_structure(directory_path, indent=0):
    directory = Path(directory_path)

    if not directory.is_dir():
        print (Fore.RED + f"Директорія не існує або не є директорією: {directory_path}")
        return
    
    
    for item in directory.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.BLUE + f"📂 {item.name}/")
            display_directory_structure(item, indent + 4)

        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати лише один аргумент - шлях до директорії.")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    display_directory_structure(directory_path)