import os
from datetime import datetime

# Function to create a new diary entry
def create_entry(filename):
    try:
        # Ask the user to input their diary entry
        print("\nPlease enter your diary entry. Type 'exit' when you're done.")
        entry = ""
        while True:
            line = input()
            if line.lower() == 'exit':
                break
            entry += line + '\n'

        # Optionally, add a timestamp to the entry
        add_timestamp = input("\nWould you like to add a timestamp to your entry? (y/n): ").strip().lower()
        if add_timestamp == 'y':
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"Timestamp: {timestamp}\n\n" + entry
        
        # Open the file in append mode to add the new entry
        with open(filename, 'a') as file:
            file.write(entry)
            file.write("\n" + "-"*50 + "\n")  # Separator for different entries

        print("\nYour diary entry has been saved!")

    except PermissionError:
        print("\nError: You don't have permission to write to this file.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# Function to view previous diary entries
def view_entries(filename):
    try:
        # Check if the file exists
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                entries = file.read()
                if entries.strip():  # Ensure there's something to display
                    print("\nPrevious Diary Entries:")
                    print(entries)
                else:
                    print("\nNo entries found.")
        else:
            print("\nNo diary file found. Please create a new entry first.")

    except FileNotFoundError:
        print("\nError: Diary file not found.")
    except PermissionError:
        print("\nError: You don't have permission to read this file.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# Main function to drive the program
def main():
    filename = "diary.txt"
    
    while True:
        # Menu for the user
        print("\nPersonal Diary Application")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            create_entry(filename)
        elif choice == '2':
            view_entries(filename)
        elif choice == '3':
            print("\nGoodbye! Your diary is always here when you need it.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
