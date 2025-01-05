# lib/helpers.py
from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime 

def add_new_athlete():
    """Helper function to add a new athlete"""
    print("\n=== Add New Athlete ===")
    try:
        name = input("Enter athlete name: ")
        position = input("Enter athlete position: ")

        athlete = Athlete.create(name, position)
        print(f"\nSuccessfully added {name}!")
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please try again.")

def view_all_athletes():
    """Helper function to display all athletes"""
    print("\n=== All Athletes ===")
    athletes = Athlete.get_all()
    if not athletes:
        print("No athletes found.")
        return
    
    for athlete in athletes:
        print(f"\nName: {athlete.name}")
        print(f"Position: {athlete.position}")

def find_athlete():
    """Helper function to find athlete by name"""
    name = input("\nEnter athlete name to search: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        print(f"\nFound athlete:")
        print(f"Name: {athlete.name}")
        print(f"Position: {athlete.position}")
    else:
        print(f"\nNo athlete found with name: {name}")

def update_athlete():
    """Helper function to update athlete information"""
    name = input("\nEnter athlete name to update: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        try:
            print("\nEnter new information (press enter to keep current value):")
            
            new_name = input(f"Name ({athlete.name}): ")
            new_position = input(f"Position ({athlete.position}): ")
            
            if new_name.strip(): athlete.name = new_name
            if new_position.strip(): athlete.position = new_position
            
            athlete.update()
            print(f"\nSuccessfully updated {athlete.name}!")
        except ValueError as e:
            print(f"\nError: {e}")
            print("Update failed. Please try again.")
    else:
        print(f"\nNo athlete found with name: {name}")

def delete_athlete():
    """Helper function to delete an athlete"""
    name = input("\nEnter athlete name to delete: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        confirm = input(f"\nAre you sure you want to delete {name}? (y/n): ")
        if confirm.lower() == 'y':
            athlete.delete()
            print(f"\nDeleted {name}")
        else:
            print("\nDeletion cancelled")
    else:
        print(f"\nNo athlete found with name: {name}")

def record_performance():
    """Helper function to record new performance test results"""
    while True:
        name = input("\nEnter athlete name: ")
        athlete = Athlete.find_by_name(name)
        if athlete:
            try:
                print("\nEnter test results:")
                speed_score = float(input("Speed score (0-10): "))
                strength_score = float(input("Strength score (0-10): "))
                notes = input("Notes (optional): ")
                
                performance = Performance.create(
                    athlete_id=athlete.id,
                    test_date=datetime.now().strftime('%Y-%m-%d'),
                    speed_score=speed_score,
                    strength_score=strength_score,
                    notes=notes
                )
                print("\nPerformance recorded successfully!")
                break
            except ValueError as e:
                print(f"\nError: {e}")
                print("Please try again.")
        else:
            print(f"\nNo athlete found with name: {name}")
            retry = input("Would you like to try another name? (y/n): ")
            if retry.lower() != 'y':
                break

def view_athlete_performance():
    """Helper function to view an athlete's test history"""
    name = input("\nEnter athlete name: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        performances = athlete.get_performances()
        if not performances:
            print(f"\nNo performances found for {name}")
            return
        
        for perf in performances:
            print(f"\nTest Date: {perf.test_date}")
            print(f"Speed Score: {perf.speed_score}")
            print(f"Strength Score: {perf.strength_score}")
            if perf.notes:
                print(f"Notes: {perf.notes}")
    else:
        print(f"\nNo athlete found with name: {name}")

def find_top_performers():
    """Helper function to find top performers in each category"""
    athletes = Athlete.get_all()
    if not athletes:
        print("\nNo athletes found.")
        return
    
    found_performances = False
    for athlete in athletes:
        try:
            performances = athlete.get_performances()
            if performances:
                found_performances = True
                best_speed = max((p.speed_score for p in performances), default=None)
                best_strength = max((p.strength_score for p in performances), default=None)
                
                print(f"\nAthlete: {athlete.name}")
                if best_speed:
                    print(f"Best speed score: {best_speed}")
                if best_strength:
                    print(f"Best strength score: {best_strength}")
        except Exception as e:
            print(f"\nError processing data for {athlete.name}: {e}")
    
    if not found_performances:
        print("\nNo performance records found for any athlete.")

def track_progress():
    """Helper function to track an athlete's progress over time"""
    name = input("\nEnter athlete name: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        performances = athlete.get_performances()
        if len(performances) < 2:
            print(f"\nNeed at least 2 performances to track progress for {name}")
            return
        
        first = performances[-1]  # Oldest performance
        last = performances[0]    # Most recent performance
        
        print(f"\nProgress for {name}:")
        print(f"Speed score: {first.speed_score} → {last.speed_score}")
        print(f"Strength score: {first.strength_score} → {last.strength_score}")

def exit_program():
    """Helper function to exit the program"""
    print("\nGoodbye!")
    exit()