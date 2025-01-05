class EmployeeNode:
    def __init__(self, e_id, name, designation, salary):
        self.e_id = e_id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.next = None  

class EmployeeLinkedList:
    def __init__(self):
        self.head = None  
        self.size = 0  

    def insert_employee(self, e_id, name, designation, salary):
        new_node = EmployeeNode(e_id, name, designation, salary)  

        if self.size == 10:  
            self.delete_last_employee()  
        if not self.head:  
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node

        self.size += 1  
    
    def search_employee(self, e_id):
        current = self.head
        while current:
            if current.e_id == e_id:  
                return current
            current = current.next
        return None  

    
    def display_all(self):
        current = self.head
        employees = []
        while current:
            employees.append((current.e_id, current.name, current.designation, current.salary)) 
            current = current.next
        return employees  
        


    def delete_last_employee(self):
        if not self.head:  
            return False

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return True

        current = self.head
        while current.next and current.next.next:
            current = current.next

        current.next = None
        self.size -= 1
        return True

def main():
    employee_list = EmployeeLinkedList()  
    employee_list.insert_employee(1, "MUGISHA JEAN PAUL", "Software Engineer", 50000)
    employee_list.insert_employee(2, "KANYARWANDA ALICE", "Data Scientist", 60000)
    employee_list.insert_employee(3, "NDAYISENGA PAUL", "Project Manager", 70000)
    employee_list.insert_employee(4, "UMURUNGI GRACE", "HR Manager", 55000)
    employee_list.insert_employee(5, "NTAMBARA JOHN", "Marketing Specialist", 48000)

    employees = employee_list.display_all()
    print("\n\nAll Employees:")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}, Salary: {emp[3]}")

    print("\nSearch for Employee with ID 2:\n")
    employee = employee_list.search_employee(2)
    if employee:
        print(f"Employee Found: ID: {employee.e_id}, Name: {employee.name}, Designation: {employee.designation}, Salary: {employee.salary}")
    else:
        print("Employee not found.")

    print("\nDeleting Last Employee:\n")
    employee_list.delete_last_employee()

    employees = employee_list.display_all()
    print("\nUpdated Employee List:\n")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}, Salary: {emp[3]}")
    print("\n")

if __name__ == "__main__":
    main()
