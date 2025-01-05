# Class to represent a node in the linked list for employee data
class EmployeeNode:
    def __init__(self, e_id, name, designation, salary):
        # Initialize employee node with the given attributes
        self.e_id = e_id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.next = None  # Set the next reference to None initially

# Class to manage the linked list of employees
class EmployeeLinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with no employees
        self.size = 0  # Track the size of the list
    
    # Insert employee at the end of the list
    def insert_employee(self, e_id, name, designation, salary):
        new_node = EmployeeNode(e_id, name, designation, salary)  # Create a new employee node
        if not self.head:  # If the list is empty, set the new node as head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list and add the new node
                current = current.next
            current.next = new_node
        self.size += 1  # Increment the list size
    
    # Search for an employee by ID
    def search_employee(self, e_id):
        current = self.head
        while current:
            if current.e_id == e_id:  # If employee found, return the node
                return current
            current = current.next
        return None  # If not found, return None
    
    # Get the list of all employees for display
    def display_all(self):
        current = self.head
        employees = []
        while current:
            employees.append((current.e_id, current.name, current.designation, current.salary))  # Collect employee data
            current = current.next
        return employees  # Return the list of all employee records
    
    # Delete an employee by ID
    def delete_employee(self, e_id):
        current, prev = self.head, None
        while current:
            if current.e_id == e_id:  # If employee found
                if prev:  # If it's not the first employee in the list
                    prev.next = current.next
                else:  # If it's the first employee in the list
                    self.head = current.next
                self.size -= 1  # Decrease the size of the list
                return True  # Successfully deleted the employee
            prev, current = current, current.next
        return False  # Employee not found

    # Update an employee's details
    def update_employee(self, e_id, name=None, designation=None, salary=None):
        current = self.head
        while current:
            if current.e_id == e_id:
                if name:
                    current.name = name
                if designation:
                    current.designation = designation
                if salary:
                    current.salary = salary
                return True
            current = current.next
        return False  # Employee not found

# Main application class to handle operations via console input
class PayrollApp:
    def __init__(self):
        self.employee_list = EmployeeLinkedList()  # Create an instance of the EmployeeLinkedList
    
    # Function to display the menu options
    def display_menu(self):
        print("\nSaaS-Based Payroll System for Startups")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Display All Employees")
        print("6. Exit")
    
    # Function to add a new employee
    def add_employee(self):
        e_id = int(input("Enter Employee Code: "))
        name = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))
        self.employee_list.insert_employee(e_id, name, designation, salary)
        print("Employee added successfully!")
    
    # Function to search for an employee by ID
    def search_employee(self):
        e_id = int(input("Enter Employee Code to search: "))
        employee = self.employee_list.search_employee(e_id)
        if employee:
            print(f"\nEmployee Found\nID: {employee.e_id}\nName: {employee.name}\nDesignation: {employee.designation}\nSalary: {employee.salary}")
        else:
            print("Employee not found.")
    
    # Function to update an employee's details
    def update_employee(self):
        e_id = int(input("Enter Employee Code to update: "))
        name = input("Enter new Name (leave blank to skip): ")
        designation = input("Enter new Designation (leave blank to skip): ")
        salary = input("Enter new Salary (leave blank to skip): ")
        
        if salary:
            salary = float(salary)
        else:
            salary = None
        
        updated = self.employee_list.update_employee(e_id, name if name else None, designation if designation else None, salary)
        if updated:
            print("Employee details updated successfully!")
        else:
            print("Employee not found.")
    
    # Function to delete an employee by ID
    def delete_employee(self):
        e_id = int(input("Enter Employee Code to delete: "))
        if self.employee_list.delete_employee(e_id):
            print(f"Employee {e_id} deleted successfully!")
        else:
            print("Employee not found.")
    
    # Function to display all employees
    def display_all_employees(self):
        employees = self.employee_list.display_all()
        if not employees:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}, Salary: {emp[3]}")
    
    # Function to run the application
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.search_employee()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.display_all_employees()
            elif choice == "6":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

# Main entry point of the program
if __name__ == "__main__":
    app = PayrollApp()
    app.run()
