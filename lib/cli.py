# cli.py
from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime

def main_menu():
    while True:
        print("\n=== Athlete Performance Tracker ===")
        print("1. Add Athlete")
        print("2. View All Athletes")
        print("3. Add Performance")
        print("4. View Athlete's Performances")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_athlete()
        elif choice == "2":
            view_athletes()
        elif choice == "3":
            add_performance()
        elif choice == "4":
            view_performances()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_athlete():
    name = input("Enter athlete name: ")
    position = input("Enter athlete position: ")
    try:
        athlete = Athlete(name, position)
        athlete.save()
        print(f"Added athlete: {name}")
    except ValueError as e:
        print(f"Error: {e}")

def view_athletes():
    athletes = Athlete.get_all()
    if not athletes:
        print("No athletes found.")
        return
    
    for athlete in athletes:
        print(f"ID: {athlete.id}, Name: {athlete.name}, Position: {athlete.position}")

def add_performance():
    athlete_name = input("Enter athlete name: ")
    athlete = Athlete.find_by_name(athlete_name)
    if not athlete:
        print("Athlete not found.")
        return

    try:
        date = input("Enter test date (YYYY-MM-DD): ")
        speed = float(input("Enter speed score (0-10): "))
        strength = float(input("Enter strength score (0-10): "))
        notes = input("Enter notes (optional): ")

        performance = Performance(
            athlete.id,
            date,
            speed,
            strength,
            notes
        )
        performance.save()
        print("Performance recorded successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def view_performances():
    athlete_name = input("Enter athlete name: ")
    athlete = Athlete.find_by_name(athlete_name)
    if not athlete:
        print("Athlete not found.")
        return

    performances = athlete.get_performances()
    if not performances:
        print("No performances recorded for this athlete.")
        return

    for p in performances:
        print(f"\nDate: {p.test_date}")
        print(f"Speed Score: {p.speed_score}")
        print(f"Strength Score: {p.strength_score}")
        if p.notes:
            print(f"Notes: {p.notes}")

if __name__ == "__main__":
    Athlete.create_table()
    Performance.create_table()
    main_menu()