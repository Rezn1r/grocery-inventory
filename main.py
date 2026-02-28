from menus import auth_menu
from database import init_db

def main():
    init_db()
    auth_menu()

if __name__ == "__main__":
    main()