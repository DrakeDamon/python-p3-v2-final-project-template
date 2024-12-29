# lib/cli.py
from models.athlete import Athlete
from models.performance import Performance



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
            print("\nInvalid choice")


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
            
def update_performance_menu():
    # First, get athlete's performances
    athlete_id = input("Enter athlete ID: ")
    performances = Performance.get_by_athlete_id(athlete_id)
    
    if not performances:
        print("No performances found for this athlete.")
        return

    # Show available performances
    print("\nAvailable Performances:")
    for i, perf in enumerate(performances):
        print(f"{i+1}. Date: {perf.test_date}, 40yd: {perf.forty_yard}")
    
    # Get which performance to update
    choice = input("\nEnter number of performance to update: ")
    try:
        performance = performances[int(choice)-1]
    except (ValueError, IndexError):
        print("Invalid selection")
        return

    # Get updated values
    print("\nEnter new values (press enter to keep current value):")
    
    new_date = input(f"Test date [{performance.test_date}]: ")
    new_forty = input(f"40-yard time [{performance.forty_yard}]: ")
    new_vertical = input(f"Vertical jump [{performance.vertical_jump}]: ")
    new_agility = input(f"Agility time [{performance.agility_time}]: ")
    new_flexibility = input(f"Flexibility score [{performance.flexibility_score}]: ")
    new_strength = input(f"Strength score [{performance.strength_score}]: ")
    new_notes = input(f"Notes [{performance.notes}]: ")

    # Update only if new value provided
    if new_date: performance.test_date = new_date
    if new_forty: performance.forty_yard = float(new_forty)
    if new_vertical: performance.vertical_jump = float(new_vertical)
    if new_agility: performance.agility_time = float(new_agility)
    if new_flexibility: performance.flexibility_score = float(new_flexibility)
    if new_strength: performance.strength_score = float(new_strength)
    if new_notes: performance.notes = new_notes

    # Save updates
    try:
        performance.update()
        print("\nPerformance updated successfully!")
    except Exception as e:
        print(f"\nError updating performance: {e}")

# In main menu loop
while True:
    print("\nAthletic Performance Tracker")
    print("1. Add Performance")
    print("2. View Performances")
    print("3. Update Performance")
    print("4. Delete Performance")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "3":
        update_performance_menu()

def analysis_menu():
    while True:
        print("\n=== Analysis ===")
        print("1. Find Top Performers")
        print("2. Track Progress")
        print("3. Return to Main Menu")

        choice = input("\nEnter your choices:")

        if choice == "1":
            find_top_performers()
        elif choice == "2":
            track_progress()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    Athlete.create_table()
    Performance.create_table()
    main()
