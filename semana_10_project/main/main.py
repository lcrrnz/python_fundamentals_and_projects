import sys
sys.path.append("C:/Users/Coqui/Documents/Curso Python/lifter/my_first_repository/Semana_10_project")

from menu.student_data_base_menu import data_base_menu

def execution():
    try:
        if __name__ == "__main__":
            data_base_menu()
    except Exception as error:
        print(f"Fatal error encountered: {error}")


execution()