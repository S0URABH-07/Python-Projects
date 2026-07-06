import os
from src.roster import RosterManager

def display_menu():
    print("\n====== EMPLOYEE RECORD SYSTEM ======")
    print("1. Register New Employee Profile")
    print("2. Print Complete Roster Spreadsheet")
    print("3. Search Employee by Unique ID")
    print("4. Update Designation & Salary")
    print("5. Delete Worker Profile From Logs")
    print("6. Save Changes & Exit System")
    print("====================================")

def main():
    data_directory = "data"
    file_path = os.path.join(data_directory, "employees.csv")
    
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    hr_system = RosterManager(file_path)
    
    while True:
        display_menu()
        choice = input("Select administrative action (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Register New Employee ---")
            emp_id = input("Enter Unique Employee ID: ").strip()
            name = input("Enter Employee Full Name: ").strip()
            dept = input("Enter Department Division: ").strip()
            role = input("Enter Active Job Title/Role: ").strip()
            
            try:
                salary = float(input("Enter Monthly Salary: ₹"))
            except ValueError:
                print("Error: Salary input parameters must be a clean numeric format!")
                continue
                
            hr_system.add_employee(emp_id, name, dept, role, salary)
            
        elif choice == "2":
            hr_system.display_roster()
            
        elif choice == "3":
            print("\n--- Profile Identification Search ---")
            emp_id = input("Enter Employee ID to track: ").strip()
            hr_system.search_employee(emp_id)
            
        elif choice == "4":
            print("\n--- Update Corporate Profile Details ---")
            emp_id = input("Enter target Employee ID: ").strip()
            employee = hr_system.search_employee(emp_id)
            
            if employee != None:
                new_role = input("Enter New Job Title/Role: ").strip()
                try:
                    new_salary = float(input("Enter Updated Salary: ₹"))
                except ValueError:
                    print("Error: Numeric input required for monetary configuration!")
                    continue
                employee.update_profile(new_role, new_salary)
                
        elif choice == "5":
            print("\n--- Terminate Worker Profile Record ---")
            emp_id = input("Enter Employee ID to purge from roster: ").strip()
            hr_system.remove_employee(emp_id)
            
        elif choice == "6":
            print("\nSyncing local adjustments back to spreadsheet storage...")
            hr_system.save_to_csv()
            print("Database channel locked securely. Operation complete!")
            break
            
        else:
            print("Invalid administration command! Please select an input option from 1 to 6.")

if __name__ == "__main__":
    main()