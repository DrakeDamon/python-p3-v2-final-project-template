# lib/helpers.py
from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime 

def add_new_athlete():
    """Helper function to add a new athlete"""
    print("\n=== Add New Athlete ===")
    try:
        name = input("Enter athlete name: ")
        height = float(input("Enter athlete height (in inches): "))
        weight = float(input("Enter athlete weight (in lbs): "))
        position = input("Enter athlete position: ")

        athlete = Athlete(name, height, weight, position)
        athlete.save()
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
        print(f"Height: {athlete.height} inches")
        print(f"Weight: {athlete.weight} lbs")
        print(f"Position: {athlete.position}")

def find_athlete():
    """Helper function to find athlete by name"""
    name = input("\nEnter athlete name to search: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        print(f"\nFound athlete:")
        print(f"Name: {athlete.name}")
        print(f"Height: {athlete.height} inches")
        print(f"Weight: {athlete.weight} lbs")
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
            new_height = input(f"Height in inches ({athlete.height}): ")
            new_weight = input(f"Weight in lbs ({athlete.weight}): ")
            new_position = input(f"Position ({athlete.position}): ")
            
            if new_name.strip(): athlete.name = new_name
            if new_height.strip(): athlete.height = float(new_height)
            if new_weight.strip(): athlete.weight = float(new_weight)
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
    name = input("\nEnter athlete name: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        try:
            print("\nEnter test results:")
            forty_yard = float(input("40-yard dash time (seconds): "))
            vertical = float(input("Vertical jump height (inches): "))
            agility = float(input("5-10-5 agility time (seconds): "))
            flexibility = float(input("Flexibility score: "))
            strength = float(input("Strength score: "))
            notes = input("Notes (optional): ")
            
            performance = Performance(
                athlete_id=athlete.id,
                test_date=datetime.now(),
                forty_yard=forty_yard,
                vertical_jump=vertical,
                agility_time=agility,
                flexibility_score=flexibility,
                strength_score=strength,
                notes=notes
            )
            performance.save()
            print("\nPerformance recorded successfully!")
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please try again.")
    else:
        print(f"\nNo athlete found with name: {name}")

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
            print(f"\nTest Date: {perf.test_date.strftime('%Y-%m-%d')}")
            print(f"40-yard dash: {perf.forty_yard:.2f} seconds")
            print(f"Vertical jump: {perf.vertical_jump:.2f} inches")
            print(f"Agility time: {perf.agility_time:.2f} seconds")
            print(f"Flexibility: {perf.flexibility_score}")
            print(f"Strength: {perf.strength_score}")
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
    
    for athlete in athletes:
        performances = athlete.get_performances()
        if performances:
            best_forty = min((p.forty_yard for p in performances), default=None)
            best_vertical = max((p.vertical_jump for p in performances), default=None)
            
            print(f"\nAthlete: {athlete.name}")
            if best_forty:
                print(f"Best 40-yard dash: {best_forty:.2f} seconds")
            if best_vertical:
                print(f"Best vertical jump: {best_vertical:.2f} inches")

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
        print(f"40-yard dash: {first.forty_yard:.2f} → {last.forty_yard:.2f} seconds")
        print(f"Vertical jump: {first.vertical_jump:.2f} → {last.vertical_jump:.2f} inches")
        print(f"Agility time: {first.agility_time:.2f} → {last.agility_time:.2f} seconds")
        print(f"Flexibility: {first.flexibility_score:.2f} → {last.flexibility_score:.2f}")
        print(f"Strength: {first.strength_score:.2f} → {last.strength_score:.2f}")

def exit_program():
    """Helper function to exit the program"""
    print("\nGoodbye!")
    exit()