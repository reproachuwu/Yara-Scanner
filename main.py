import os
import yara
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import time
import threading
from itertools import cycle
from random import randint
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)


x = []

def scan_file(file_path, yara_rules):
    try:
        with open(file_path, 'rb') as f:
            matches = yara_rules.match(data=f.read())
            if matches:
                print(f" [\033[92m+\033[0m] Match found in file: {file_path}")
                x.append(file_path)
               
    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")

def scan_files(yara_rules, path):
    with ThreadPoolExecutor(max_workers=48) as executor:
        futures = []
        for root, dirs, files in os.walk(path):
            print(f" [\033[93m+\033[0m] {root}.")
            for file in files:
                file_path = os.path.join(root, file)
                futures.append(executor.submit(scan_file, file_path, yara_rules))
        
        for future in as_completed(futures):    
            future.result()  
    print("Scan completed.")

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{Fore.CYAN}{bar}{Style.RESET_ALL}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()

def main():
    global x  # Use the global x list
    os.system('cls' if os.name == 'nt' else 'clear')

    print("", Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + "Welcome to Yara Scanner".center(60))
    print("", Fore.YELLOW + "=" * 60 + Style.RESET_ALL)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    yara_rules_path = os.path.join(current_dir, 'yara.yar')
    try:
        yara_rules = yara.compile(yara_rules_path)
        print("\n [\033[92m+\033[0m] YARA rules compiled successfully")
    except Exception as e:
        print(Fore.RED + f" [✗] Error compiling YARA rules: {e}" + Style.RESET_ALL)
        return

    # Get path to scan from user
    path = input(f"\n [{Fore.RED}?{Style.RESET_ALL}] Enter base path to scan: ")
    print(Fore.YELLOW + "\nScanning files... Please wait.\n" + Style.RESET_ALL)

    # Scan files in the given path
    scan_files(yara_rules, path)

    # Remove any entry containing "yara.yar" from the matches list
    x = [match for match in x if "yara.yar" not in match]

    # Create and populate the PrettyTable
    table = PrettyTable()
    table.field_names = [Fore.CYAN + "Matched Files" + Style.RESET_ALL]
    for match in x:
        table.add_row([Fore.GREEN + match + Style.RESET_ALL])

    # Set the alignment and max width for the column
    table.align["Matched Files"] = "l"
    table.max_width["Matched Files"] = 80

    print(Fore.YELLOW + "\nScan Results:" + Style.RESET_ALL)
    print(table)

    input(Fore.MAGENTA + "\nPress Enter to exit..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
    input("")