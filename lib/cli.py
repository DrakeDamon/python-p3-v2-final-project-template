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
    print("4. Exit")

def athlete_menu():
    while True:
        print("\n=== Athlete Management ===")
        print("1. Add New Athlete")
        print("2. View All Athletes")
        print("3. Find Athlete")
        print("4. Update Athlete")
        print("5. Delete Athlete")
        print("6. Return to Main Menu")

        choice = input("\nEnter your choices:")

        if choice == "1":
            add_new_athlete()
        elif choice == "2":
            view_all_athletes()
        elif choice == "3":
            find_athlete()
        elif choice == "4":
            update_athlete()
        elif choice == "5":
            delete_athlete()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


def performance_menu():
    while True:
        print("\n=== Performance Testing ===")
        print("1. Record New Performance")
        print("2. View Athlete's Performance History")
        print("3. Return to Main Menu")

        choice = input("\nEnter your choices:")

        if choice == "1":
            record_performance()
        elif choice == "2":
            view_athlete_performance()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
