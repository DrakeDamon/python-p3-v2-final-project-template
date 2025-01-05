# cli.py
from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime

def main_menu():
    while True:
        print("\n=== Athlete Performance Tracker ===")
        print("1. View Athletes")
        print("2. Add New Athlete")
        print("3. Record Performance")
        print("4. View Performance History")
        print("5. Delete Athlete")        # New option
        print("6. Delete Performance")    # New option
        print("7. Exit")
        
        choice = input("\nWhat would you like to do? (1-7): ")
        
        if choice == "1":
            athlete_menu()
        elif choice == "2":
            add_athlete()
        elif choice == "3":
            record_performance()
        elif choice == "4":
            view_performance_history()
        elif choice == "5":
            delete_athlete()
        elif choice == "6":
            delete_performance()
        elif choice == "7":
            print("\nThank you for using Athlete Performance Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def athlete_menu():
    while True:
        athletes = view_athletes()
        if not athletes:
            input("\nPress Enter to return to main menu...")
            return

        print("\nWhat would you like to do?")
        print("1. Select an athlete")
        print("2. Return to main menu")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            select_and_manage_athlete(athletes)
        elif choice == "2":
            break

def view_athletes():
    """Display all athletes"""
    print("\n=== Athletes ===")
    athletes = Athlete.get_all()
    if not athletes:
        print("No athletes registered yet.")
        return None
    
    for i, athlete in enumerate(athletes, 1):
        print(f"{i}. {athlete.name} - {athlete.position}")
    return athletes

def select_and_manage_athlete(athletes):
    """Let user select and manage a specific athlete"""
    while True:
        try:
            choice = input("\nSelect athlete number: ")
            if choice.lower() == 'back':
                return
            
            index = int(choice) - 1
            if 0 <= index < len(athletes):
                athlete = athletes[index]
                manage_athlete(athlete)
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def manage_athlete(athlete):
    """Menu for managing a specific athlete"""
    while True:
        print(f"\n=== {athlete.name}'s Profile ===")
        print("1. Record New Performance")
        print("2. View Performance History")
        print("3. Return to Athletes List")
        
        choice = input("\nWhat would you like to do? (1-3): ")
        
        if choice == "1":
            record_performance(athlete)
        elif choice == "2":
            view_athlete_performances(athlete)
        elif choice == "3":
            break

def add_athlete():
    print("\n=== Add New Athlete ===")
    try:
        name = input("Enter athlete name: ")
        position = input("Enter position: ")
        athlete = Athlete.create(name, position)
        print(f"\nSuccessfully added {name}!")
    except ValueError as e:
        print(f"\nError: {e}")
def record_performance(selected_athlete=None):
    print("\n=== Record Performance ===")
    try:
        if not selected_athlete:
            athletes = view_athletes()
            if not athletes:
                return
            
            athlete_num = input("\nSelect athlete number: ")
            try:
                selected_athlete = athletes[int(athlete_num) - 1]
            except (ValueError, IndexError):
                print("Invalid selection.")
                return
        print("\nEnter test result: ")
        speed = float(input(f"\nEnter {selected_athlete.name}'s speed score (0-10): "))
        date_str = input("\nEnter test date MM/DD/YYYY: ")
        strength = float(input("Enter strength score (0-10): "))
        notes = input("Add any notes (optional): ").strip()
        notes = notes if notes else None

        performance = Performance.create(
            athlete_id=selected_athlete.id,
            test_date=datetime.now().strftime('%Y-%m-%d'),
            speed_score=speed,  
            strength_score=strength, 
            notes=notes
        )
        print("\nPerformance recorded successfully!")
    except ValueError as e:
        print(f"\nError: {e}")

def view_performance_history():
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number: ")
        athlete = athletes[int(athlete_num) - 1]
        view_athlete_performances(athlete)
    except (ValueError, IndexError):
        print("Invalid selection.")

def view_athlete_performances(athlete):
    print(f"\n=== {athlete.name}'s Performance History ===")
    performances = athlete.get_performances()
    if not performances:
        print("No performances recorded yet.")
        return

    for perf in performances:
        print(f"\nDate: {perf.test_date}")
        print(f"Speed Score: {perf.speed_score}/10")
        print(f"Strength Score: {perf.strength_score}/10")
        if perf.notes:
            print(f"Notes: {perf.notes}")
    
    input("\nPress Enter to continue...")

def delete_athlete():
    print("\n=== Delete Athlete ===")
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number to delete (or 'back' to return): ")
        if athlete_num.lower() == 'back':
            return
            
        athlete = athletes[int(athlete_num) - 1]
        confirm = input(f"\nAre you sure you want to delete {athlete.name}? (y/n): ")
        
        if confirm.lower() == 'y':
            athlete.delete()
            print(f"\n{athlete.name} has been deleted.")
        else:
            print("\nDeletion cancelled.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def delete_performance():
    print("\n=== Delete Performance ===")
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number: ")
        athlete = athletes[int(athlete_num) - 1]
        
        performances = athlete.get_performances()
        if not performances:
            print(f"\nNo performances found for {athlete.name}")
            return
            
        print(f"\n{athlete.name}'s Performances:")
        for i, perf in enumerate(performances, 1):
            print(f"\n{i}. Date: {perf.test_date}")
            print(f"   Speed Score: {perf.speed_score}/10")
            print(f"   Strength Score: {perf.strength_score}/10")
        
        perf_num = input("\nSelect performance number to delete (or 'back' to return): ")
        if perf_num.lower() == 'back':
            return
            
        try:
            performance = performances[int(perf_num) - 1]
            confirm = input(f"\nAre you sure you want to delete this performance? (y/n): ")
            
            if confirm.lower() == 'y':
                try:
                    performance.delete()
                    print("\nPerformance has been deleted.")
                except ValueError as e:
                    print(f"\nError deleting performance: {e}")
            else:
                print("\nDeletion cancelled.")
        except (ValueError, IndexError):
            print("\nInvalid performance number.")
    except (ValueError, IndexError):
        print("\nInvalid athlete number.")

if __name__ == "__main__":
    Athlete.create_table()
    Performance.create_table()
    main_menu()