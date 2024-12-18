from datetime import datetime
import csv
import sys

# Display the main menu
def display_menu():
    print("\nMenu:")
    print("1. Log a new entry")
    print("2. View all entries")
    print("3. View summary")
    print("4. Delete entry")
    print("5. Quit")

# Validate the date format (DD/MM/YY)
def is_valid_date(date):
    try:
        check_return(date)  
        # Check if date matches dd/mm/yy format
        datetime.strptime(date, "%d/%m/%y")
        return True
    except ValueError:
        return False

# Validate if the amount is a valid number
def is_valid_amount(amount):
    try:
        check_return(amount)  
        float(amount)
        return True
    except ValueError:
        return False

# Categories available for entry
categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]

# Validate if the input category is valid
def is_valid_category(category):
    check_return(category)  
    return category in categories

# Check if the entry already exists in the CSV file
def is_duplicate_entry(entry):
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Date'] == entry['Date'] and row['Category'] == entry['Category'] and float(row['Amount']) == entry['Amount']:
                    return True
        return False
    except FileNotFoundError:
        main()  # file not found error

# Check if the file exists
def check_file_exists():
    try:
        with open('expenses.csv', mode='r'):
            pass
    except FileNotFoundError:
        print("\nNo entries yet: Type in a new entry to start the expenses.csv file")
        main()

def check_return(value) : 
    if value.lower() == 'return':
        main()

# Search entries based on criteria
def search_entries():
    print("\nSearch options:")
    print("1. Search by Date")
    print("2. Search by Amount")
    print("3. Search by Category")
    print("4. Cancel")
    
    while True:
        choice = input("Choose an option: ")
        if is_valid_amount(choice):
            if 0< int(choice)<5:
                break
        else:
            print("Invalid choice. Please try again.")

    print("\nTo return to main page type 'return' at any point during the deletion process")     
    entries = []
    if choice == "1":
        while True:
            date_input = input("Enter the date to search (DD/MM/YY): ")
            check_return(date_input)
            if is_valid_date(date_input):
                with open('expenses.csv', mode='r') as file:
                    reader = csv.DictReader(file)
                    entries = [row for row in reader if row['Date'] == date_input]
                break 
            else:
                print("Not a valid date")

    elif choice == "2":
        while True:
            amount_input = input("Enter the amount to search: ")
            check_return(amount_input)
            if is_valid_amount(amount_input):
                amount_input = float(amount_input)
                with open('expenses.csv', mode='r') as file:
                    reader = csv.DictReader(file)
                    entries = [row for row in reader if round(float(row['Amount'])) == round(float(amount_input))]
                break
            else:
                print("Not a valid amount")

    
    
    elif choice == "3":
        while True:
            print("\nCategories: Food, Transport, Entertainment, Utilities, Other")
            category_input = input("Enter the category to search: ").capitalize()
            check_return(category_input)
            if is_valid_category(category_input):
                with open('expenses.csv', mode='r') as file:
                    reader = csv.DictReader(file)
                    entries = [row for row in reader if row['Category'] == category_input]
                break
            else:
                print("\nNot a valid category")
    
    elif choice == "4":
        main()
    
    return entries

# Function to delete an entry
def delete_entry():
    check_file_exists()  # Ensure the file exists before proceeding
    
    entries = search_entries()

    if not entries:
        print("\nNo entries found that match your criteria.")
        return
    
    # Display the results with numbered rows
    print("\nMatching Entries:")
    print(f"{'No.':<5}{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}")
    for idx, row in enumerate(entries, start=1):
        print(f"{idx:<5}{row['Date']:<15}{row['Category']:<15}{row['Amount']:<10}{row['Description']}")

    while True:
        row_to_delete = input("\nSelect the number of the entry you want to delete: ")
        check_return(row_to_delete)

        if is_valid_amount(row_to_delete):  # Check if it's a valid number
            row_to_delete = int(row_to_delete)  # Convert to integer
            if 1 <= row_to_delete <= len(entries):  # Check if it's within the valid range
                break  # Valid row, exit the loop
            else:
                print(f"\nSelect a valid entry number between 1 and {len(entries)}")
        else:
            print("\nSelect a valid entry number")


    # Confirm deletion
    confirmation = ""
    while confirmation not in ['yes', 'y', 'no', 'n']:
        confirmation = input(f"Are you sure you want to delete entry {row_to_delete}? (yes/no): ").lower()
        check_return(confirmation)
        print("\nSelect valid confirmation (y,n)")
    
    if confirmation in ['yes', 'y']:
        # Read all entries and remove the selected one
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        # Find the entry to delete and remove it
        entry_to_delete = entries[row_to_delete - 1]
        rows = [row for row in rows if not (row['Date'] == entry_to_delete['Date'] and row['Category'] == entry_to_delete['Category'] and row['Amount'] == entry_to_delete['Amount'])]
        
        # Write the updated rows back to the file
        with open('expenses.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Date', 'Category', 'Amount', 'Description'])
            writer.writeheader()
            writer.writerows(rows)
        
        print("\nEntry deleted successfully.")
    else:
        print("\nDeletion cancelled.")

def view_entries():
    try:
        # Open the CSV file in read mode
        with open('expenses.csv', mode='r') as file:
            # Create a CSV reader object to read the file
            reader = csv.DictReader(file)

            # Read all the rows into a list
            entries = list(reader)
            
            # Sort the entries by 'Date' in descending order (most recent first)
            entries.sort(key=lambda x: datetime.strptime(x['Date'], "%d/%m/%y"), reverse=True)
            
            # Print a header for displaying entries
            print("\nSaved Entries:")
            # Print the column headers with specific spacing for alignment
            print(f"{'Date':<15}{'Category':<15}{'Amount':<10}{'Description'}")
            
            # Loop through each row in the sorted list
            for row in entries:
                # For each row, print the values under each column, formatted for alignment
                print(f"{row['Date']:<15}{row['Category']:<15}{row['Amount']:<10}{row['Description']}")
    # If the file is not found, print a message
    except FileNotFoundError:
        check_file_exists()

# Define a function to view a summary of expenses (total spent per category)
def view_summary():
    check_file_exists()  # Ensure the file exists before proceeding

    try:
        # Initialize a dictionary to track the total amount spent per category
        category_totals = {category: 0 for category in categories}
        total_spent = 0  # Variable to keep track of the overall total spent
        
        # Open the CSV file in read mode
        with open('expenses.csv', mode='r') as file:
            # Create a CSV reader object to read the file
            reader = csv.DictReader(file)
            
            # Loop through each row in the CSV file
            for row in reader:
                # Convert the 'Amount' value from string to float for calculation
                amount = float(row['Amount'])
                
                # Add the amount to the corresponding category total
                category_totals[row['Category']] += amount
                # Add the amount to the total spent
                total_spent += amount

        # Print a summary of expenses by category
        print("\nSummary:")
        # Loop through the category_totals dictionary to print the total spent per category
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
        
        # Print the overall total spent
        print("-"* 22)
        print(f"Total spent: ${total_spent:.2f}")#
    # If the file is not found, print a message
    except FileNotFoundError:
        check_file_exists()

def main():
    while True:  # Keep the menu active until the user decides to quit
        display_menu()
        choice = input("Choose an option (1, 2, 3, 4, or 5): ")
    
        if choice == "1":
            # Logging a new entry
            print("\nTo return to main page type 'return' at any point during the logging process")
        
            while True:
                date_input = input("Enter the date (DD/MM/YY): ")
                if is_valid_date(date_input):
                    break
                else:
                    print("Not a valid date")

            print("Categories: Food, Transport, Entertainment, Utilities, Other")
        
            while True:
                category_input = input("Enter the category: ").capitalize()
                if is_valid_category(category_input):
                    break
                else:
                    print("Not a Valid Category")

            while True:
                amount_input = input("Enter the amount: ")
                if is_valid_amount(amount_input):
                    amount_input = float(amount_input)
                    break
                else:
                    print("Not a valid amount")

            description_input = input("Enter a short description (optional): ")
            check_return(description_input)  

            entry = {
                "Date": date_input,
                "Category": category_input,
                "Amount": amount_input,
                "Description": description_input if description_input else 'No description'
            }

            # Open the CSV file and append the new entry
            with open('expenses.csv', mode='a', newline='') as file:
                header = ['Date', 'Category', 'Amount', 'Description']
                writer = csv.DictWriter(file, fieldnames=header)

                if file.tell() == 0:  # If file is empty, write header
                    writer.writeheader()

                # Check if entry is a duplicate
                if is_duplicate_entry(entry):
                    print("This entry already exists.")
                    main()

                writer.writerow(entry)
                print("Entry saved to 'expenses.csv'")

        elif choice == "2":
            view_entries()

        elif choice == "3":
            view_summary()

        elif choice == "4":
            delete_entry()

        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")


main()
