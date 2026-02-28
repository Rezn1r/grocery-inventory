import time
import getpass
from helpers import clear_screen, print_error, print_success, print_info, print_warning
from services.auth import create_user, authenticate_user

def login_menu():
    clear_screen()
    print("Login Menu")
    print("Please enter your credentials to login.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user = authenticate_user(username, password)

    if user:
        print_success(f"Welcome back, {user.username}!")
        time.sleep(1)

        return user
    else:
        print_error("Invalid username or password. Please try again.")
        time.sleep(1)

        return None

def register_menu():
    clear_screen()
    print("Registration Menu")
    print("Please enter your details to create a new account.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    confirm_password = getpass.getpass("Confirm Password: ")

    if password != confirm_password:

        print_error("Passwords do not match. Please try again.")
        return None

    success = create_user(username, password)

    if success:
        print_success("Account created successfully! You can now log in.")
        time.sleep(1)
        return login_menu()
    else:
        print_error("Username already taken. Please choose a different username.")
        return None

def auth_menu():
    clear_screen()
    print("Welcome to the Grocery Inventory Management System!")
    print("Please select an option:")
    print("[1] Login")
    print("[2] Register")
    print("[3] Exit")

    choice = input(">> ")

    if choice == "1":
        clear_screen()
        return login_menu()
    elif choice == "2":
        clear_screen()
        return register_menu()
    elif choice == "3":
        print("Goodbye!")
        exit(0)
    else:
        print("Invalid choice. Please try again.")
        return auth_menu()
