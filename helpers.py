"""
Helper fucntions
"""

import os
import subprocess
from colorama import Fore, Style


def print_error(message):
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")


def print_success(message):
    print(f"{Fore.GREEN}Success: {message}{Style.RESET_ALL}")


def print_info(message):
    print(f"{Fore.BLUE}Info: {message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}Warning: {message}{Style.RESET_ALL}")


def clear_screen():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)
