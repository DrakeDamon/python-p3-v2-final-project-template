# lib/helpers.py
from models.athlete import Athlete  # Fixed import (athlete not athletes)
from models.performance import Performance
from datetime import datetime 

def add_new_athlete():
    """Helper function to add a new athlete"""
    print("\n=== Add New Athlete ===")  # Fixed \n notation
    try:
        name = input("Enter athlete name: ")  # Removed colon after type hint
        height = float(input("Enter athlete height (in inches): "))  # Fixed float conversion
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
    print("\n=== All Athletes ===")  # Fixed \n notation
    athletes = Athlete.get_all()
    if not athletes:
        print("No athletes found.")
        return
    
    for athlete in athletes:
        print(f"\nName: {athlete.name}")  # Fixed \n notation and spacing
        print(f"Height: {athlete.height} inches")  # Added units
        print(f"Weight: {athlete.weight} lbs")
        print(f"Position: {athlete.position}")


def find_athlete():
    """Helper function to find athlete by name"""
    name = input("\nEnter athlete name to search: ")
    athlete = Athlete.find_by_name(name)
    if athlete:
        print(f"\nFound athlete:")
        print(f"Name: {athlete.name}")  # Fixed \n notation and spacing
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
            
            # Only update if new value provided
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


def view_all_performances():
    """Helper function to display all performance test results"""
    name = input("\nEnter athlete name:")
    athlete = Athlete.find_by_name(name)
    if athlete:
        performances = athlete.get_performances()
        if not performances:
            print(f"\nNo performances found for {name}.")
            return
        
        for perf in performances:
            print(f"\nTest Date: {perf.test_date.strftime('%Y-%m-%d')}")  # Fixed date formatting
            print(f"Forty-yard Dash Time: {perf.forty_yard:.2f} seconds")
            print(f"Vertical Jump Height: {perf.vertical_jump:.2f} inches")
            print(f"5-10-5 Agility Time: {perf.agility_time:.2f} seconds")
            print(f"Flexibility Score: {perf.flexibility_score}")
            print(f"Strength Score: {perf.strength_score}")
            if perf.notes:
                print(f"Notes: {perf.notes}")

        else:
            print(f"\nNo athletes found with name: {name}.")

def exit_program():
    print("\nGoodbye!")
    exit()