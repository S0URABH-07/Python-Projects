import csv
import os
from src.employee import Employee

class RosterManager:
    def __init__(self, file_path):
        self.file_path = file_path
        # Key: Employee ID, Value: Employee Object instance
        self.employees = {}
        
        self.load_from_csv()

    def load_from_csv(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                
                try:
                    header = next(reader)
                except StopIteration:
                    return  
                
                for row in reader:
                    if len(row) == 5:
                        emp_id, name, department, designation, salary = row
                        
                        # Rebuild the object, forcing salary back into a decimal float
                        employee_obj = Employee(emp_id, name, department, designation, float(salary))
                        self.employees[emp_id] = employee_obj
        else:
            self.employees = {}

    def save_to_csv(self):
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # 1. Write the mandatory top header structure row
            writer.writerow(["id", "name", "department", "designation", "salary"])
            
            # 2. Iterate through objects and convert them to flat row lists
            for emp_id, employee_obj in self.employees.items():
                writer.writerow(employee_obj.to_list())
                
        print("Employee roster database saved successfully.")

    def add_employee(self, emp_id, name, department, designation, salary):
        if emp_id in self.employees:
            print(f"Error: An employee with ID {emp_id} already exists!")
            return False
            
        new_worker = Employee(emp_id, name, department, designation, salary)
        self.employees[emp_id] = new_worker
        print(f"Employee {name} successfully added.")
        return True

    def display_roster(self):
        if len(self.employees) == 0:
            print("The employee roster is currently completely empty.")
            return
            
        print("\n" + "="*80)
        print(f"{'CURRENT CORPORATE EMPLOYEE ROSTER':^80}")
        print("="*80)
        for emp_id, employee_obj in self.employees.items():
            print(employee_obj)
        print("="*80 + "\n")

    def search_employee(self, emp_id):
        if emp_id in self.employees:
            print("\n--- Record Found ---")
            print(self.employees[emp_id])
            return self.employees[emp_id]
        else:
            print(f"Error: Employee with ID {emp_id} not found in database.")
            return None

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            removed = self.employees.pop(emp_id)
            print(f"Success: Removed {removed.name} from active roster logs.")
            return True
        else:
            print(f"Error: Employee ID {emp_id} does not exist.")
            return False