class Employee:
    def __init__(self, employee_id, name, department, designation, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        
        self.salary = float(salary)

    def update_profile(self, new_designation, new_salary):
        if new_salary <= 0:
            print("Error: Salary update must be a positive number!")
            return False
            
        self.designation = new_designation
        self.salary = float(new_salary)
        print(f"Profile updated successfully for ID {self.employee_id}.")
        return True

    def to_list(self):
        """
        Converts the employee object attributes into a flat ordered list.
        This allows the CSV writer to easily save it as a row in a spreadsheet.
        """
        return [
            self.employee_id,
            self.name,
            self.department,
            self.designation,
            self.salary
        ]

    def __str__(self):
        """Returns a clean, aligned layout string for terminal views."""
        return (f"ID: {self.employee_id:<6} | Name: {self.name:<20} | "
                f"Dept: {self.department:<10} | Role: {self.designation:<20} | "
                f"Salary: ₹{self.salary:,.2f}")