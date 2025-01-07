from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime

# Athlete 
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

def add_new_athlete():
    """Add a new athlete"""
    print("\n=== Add New Athlete ===")
    try:
        name = input("Enter athlete name: ")
        position = input("Enter position: ")
        athlete = Athlete.create(name, position)
        print(f"\nSuccessfully added {name}!")
    except ValueError as e:
        print(f"\nError: {e}")

def delete_athlete():
    """Delete an athlete and their performances"""
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number to delete (or 'back' to return): ")
        if athlete_num.lower() == 'back':
            return
            
        athlete = athletes[int(athlete_num) - 1]
        confirm = input(f"\nAre you sure you want to delete {athlete.name}? This will also delete all their performances. (y/n): ")
        
        if confirm.lower() == 'y':
            athlete.delete()
            print(f"\n{athlete.name} and all their performances have been deleted.")
        else:
            print("\nDeletion cancelled.")
    except (ValueError, IndexError):
        print("Invalid selection.")

# Performance 
def record_performance():
    """Record a new performance"""
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number: ")
        athlete = athletes[int(athlete_num) - 1]
        
        print("\nEnter test results:")
        speed = float(input(f"\nEnter {athlete.name}'s speed score (0-10): "))
        strength = float(input("Enter strength score (0-10): "))
        notes = input("Add any notes (optional): ").strip()
        notes = notes if notes else None

        performance = Performance.create(
            athlete_id=athlete.id,
            test_date=datetime.now().strftime('%Y-%m-%d'),
            speed_score=speed,
            strength_score=strength,
            notes=notes
        )
        print("\nPerformance recorded successfully!")
    except ValueError as e:
        print(f"\nError: {e}")

def view_performance_history():
    """View performance history for an athlete"""
    athletes = view_athletes()
    if not athletes:
        return
    
    try:
        athlete_num = input("\nSelect athlete number: ")
        athlete = athletes[int(athlete_num) - 1]
        
        performances = athlete.get_performances()
        if not performances:
            print(f"\nNo performances recorded for {athlete.name}")
            return

        print(f"\n=== {athlete.name}'s Performance History ===")
        for perf in performances:
            print(f"\nDate: {perf.test_date}")
            print(f"Speed Score: {perf.speed_score}/10")
            print(f"Strength Score: {perf.strength_score}/10")
            if perf.notes:
                print(f"Notes: {perf.notes}")
        
        input("\nPress Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid selection.")

def delete_performance():
    """Delete a specific performance"""
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
                performance.delete()
                print("\nPerformance has been deleted.")
            else:
                print("\nDeletion cancelled.")
        except (ValueError, IndexError):
            print("\nInvalid performance number.")
    except (ValueError, IndexError):
        print("\nInvalid athlete number.")

# def view_all_performances():
#     """View all performances from all athletes"""
#     print("\n=== All Performance Records ===")
    
#     athletes = Athlete.get_all()
#     if not athletes:
#         print("No athletes registered yet.")
#         return
    
#     found_performances = False
#     for athlete in athletes:
#         performances = athlete.get_performances()
#         if performances:
#             found_performances = True
#             print(f"\n{athlete.name}'s Performances:")
#             for perf in performances:
#                 print(f"\nDate: {perf.test_date}")
#                 print(f"Speed Score: {perf.speed_score}/10")
#                 print(f"Strength Score: {perf.strength_score}/10")
#                 if perf.notes:
#                     print(f"Notes: {perf.notes}")
#             print("-" * 30)  # Divider between athletes
    
#     if not found_performances:
#         print("No performances recorded for any athlete.")
#     else:
#         input("\nPress Enter to continue...")