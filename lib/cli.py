from models.athlete import Athlete
from models.performance import Performance
from datetime import datetime
from helpers import (
    view_athletes,
    add_new_athlete, 
    delete_athlete,
    record_performance,
    view_performance_history,
    delete_performance,
    view_all_performances
)

def main_menu():
    while True:
        print("\n=== Athlete Performance Tracker ===")
        print("1. Athlete Menu")        
        print("2. Performance Menu")    
        print("3. Exit")
        
        choice = input("\nWhat would you like to do? (1-3): ")
        
        if choice == "1":
            athlete_menu()
        elif choice == "2":
            performance_menu()
        elif choice == "3":
            print("\nThank you for using Athlete Performance Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def athlete_menu():
    while True:
        print("\n=== Athlete Menu ===")
        print("1. View All Athletes")
        print("2. Add New Athlete")
        print("3. Delete Athlete")
        print("4. Return to Main Menu")
        
        choice = input("\nEnter choice (1-4): ")
        if choice == "1":
            view_athletes()
        elif choice == "2":
            add_new_athlete()
        elif choice == "3":
            delete_athlete()
        elif choice == "4":
            break

def performance_menu():
    while True:
        print("\n=== Performance Menu ===")
        print("1. Record New Performance")
        print("2. View Performance History")
        print("3. Delete Performance")
        print("4. View All Performances")
        print("5. Return to Main Menu")

        choice = input("\nEnter choice (1-5): ")
        if choice == "1":
            record_performance()
        elif choice == "2":
            view_performance_history()
        elif choice == "3":
            delete_performance()
        elif choice == "4":
            view_all_performances()
        elif choice == "5":
            break

if __name__ == "__main__":
    Athlete.create_table()
    Performance.create_table()
    main_menu()