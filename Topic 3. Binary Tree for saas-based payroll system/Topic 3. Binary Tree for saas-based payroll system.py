
class EmployeeNode:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.left = None  
        self.right = None  

class PayrollBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, employee_id, name, salary):

        if self.search(employee_id):
            raise ValueError("Employee ID already exists.")

        new_node = EmployeeNode(employee_id, name, salary)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def search(self, employee_id):
        """Search for an employee by their ID."""
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.employee_id == employee_id:
                return current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None

    def get_employees(self):
        """Return a list of all employees in the tree."""
        employees = []
        self._in_order_traversal(self.root, employees)
        return employees

    def _in_order_traversal(self, root, employees):
        """In-order traversal to gather employee data."""
        if root:
            self._in_order_traversal(root.left, employees)
            employees.append((root.employee_id, root.name, root.salary))
            self._in_order_traversal(root.right, employees)

def main():
    payroll_tree = PayrollBinaryTree()

    try:
        payroll_tree.insert(1, "MUGISHA JEAN PAUL", 50000)
        payroll_tree.insert(2, "KANYARWANDA ALICE", 60000)
        payroll_tree.insert(3, "NDAYISENGA PAUL", 70000)
        payroll_tree.insert(4, "UMURUNGI GRACE", 55000)
        payroll_tree.insert(5, "NTAMBARA JOHN", 48000)
        
        print("\nEmployee Payroll Tree:")
        employees = payroll_tree.get_employees()

        if not employees:
            print("No employees in the payroll tree yet.")
        else:
            print("Employee ID | Name | Salary")
            print("-" * 40)
            for emp in employees:
                print(f"{emp[0]} | {emp[1]} | ${emp[2]:,.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
