# Entry point for the finance manager system. Initializes the GUI and routes user actions to income, expense, category, and export modules.
from graphics.main_window import main_window


if __name__ == "__main__":
    try:
        main_window()
    except Exception as error:
        print(f"Fatal error encountered: {error}")