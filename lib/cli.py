# lib/cli.py

from helpers import (
    add_new_athlete,
    view_all_athletes,
    find_athlete,
    update_athlete,
    delete_athlete,
    record_performance,
    view_athlete_performance,
    find_top_performers,
    track_progress,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("\nEnter your choices:")

        if choice == "1":
            athlete_menu()
        elif choice == "2":
            performance_menu()
        elif choice == "3":
            analysis_menu()
        elif choice == "4":
            exit_program()()
        else:
            print("n\Invalid choice")


def menu():
    print("\n=== Athlete Performance Tracker ===")
    print("1. Athlete Management")
    print("2. Performance Testing")
    print("3. Analysis")
    print("4. Performance Testing")



if __name__ == "__main__":
    main()
