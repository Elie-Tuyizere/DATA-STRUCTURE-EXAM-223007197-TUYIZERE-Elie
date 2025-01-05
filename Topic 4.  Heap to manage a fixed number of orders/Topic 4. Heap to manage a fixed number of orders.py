import tkinter as tk
from tkinter import messagebox

class MaxHeap:
    def __init__(self, max_size):
        self.heap = []
        self.max_size = max_size

    def push(self, order):
        if len(self.heap) < self.max_size:
            self.heap.append(order)
            self._heapify_up(len(self.heap) - 1)
        else:
            if order['priority'] > self.heap[0]['priority']:
                self.heap[0] = order
                self._heapify_down(0)

    def pop(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        max_order = self.heap.pop()
        self._heapify_down(0)
        return max_order

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index]['priority'] > self.heap[parent_index]['priority']:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < size and self.heap[left_child]['priority'] > self.heap[largest]['priority']:
                largest = left_child
            if right_child < size and self.heap[right_child]['priority'] > self.heap[largest]['priority']:
                largest = right_child
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class PayrollSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Order Management System")

        self.root.geometry("500x500")
        self.root.configure(bg="#f4f4f9")  

        self.max_size = 5
        self.heap = MaxHeap(self.max_size)

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Manage Payroll Orders", font=("Arial", 18, "bold"), fg="#4b4b4b", bg="#f4f4f9")
        self.title_label.pack(pady=20)

        self.order_desc_label = tk.Label(self.root, text="Order Description:", font=("Arial", 12), fg="#4b4b4b", bg="#f4f4f9")
        self.order_desc_label.pack()
        self.order_desc_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.order_desc_entry.pack(pady=5)

        self.priority_label = tk.Label(self.root, text="Order Priority (1-10):", font=("Arial", 12), fg="#4b4b4b", bg="#f4f4f9")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.priority_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Order", command=self.add_order, font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", relief="flat")
        self.add_button.pack(pady=15)

        self.orders_listbox = tk.Listbox(self.root, width=50, height=10, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2, relief="solid")
        self.orders_listbox.pack(pady=10)

        self.pop_button = tk.Button(self.root, text="Pop Order", command=self.pop_order, font=("Arial", 12, "bold"), fg="white", bg="#ff4d4d", relief="flat")
        self.pop_button.pack(pady=5)

        self.refresh_button = tk.Button(self.root, text="Refresh Orders", command=self.refresh_orders, font=("Arial", 12, "bold"), fg="white", bg="#ffa500", relief="flat")
        self.refresh_button.pack(pady=5)

    def add_order(self):
        order_desc = self.order_desc_entry.get()
        try:
            priority = int(self.priority_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Priority must be a number.")
            return
        
        if priority < 1 or priority > 10:
            messagebox.showerror("Invalid input", "Priority must be between 1 and 10.")
            return

        order = {
            'order_id': len(self.heap.heap) + 1,
            'priority': priority,
            'description': order_desc
        }

        self.heap.push(order)
        self.refresh_orders()

        self.order_desc_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def pop_order(self):
        order = self.heap.pop()
        if order:
            messagebox.showinfo("Order Popped", f"Popped order: {order['description']}")
            self.refresh_orders()
        else:
            messagebox.showwarning("No Orders", "No orders to pop.")

    def refresh_orders(self):
        self.orders_listbox.delete(0, tk.END)
        for order in self.heap.heap:
            order_display = f"ID: {order['order_id']} | Priority: {order['priority']} | Desc: {order['description']}"
            self.orders_listbox.insert(tk.END, order_display)

root = tk.Tk()
app = PayrollSystemApp(root)
root.mainloop()
