
def merge_sort(data, key):

    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left, key)
    right_sorted = merge_sort(right, key)

    return merge(left_sorted, right_sorted, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

payroll_entries = [
    { "priority": 3, "employee_id": 101, "employee_name": "Alice", "salary": 50000},
    {"priority": 1, "employee_id": 102, "employee_name": "Bob", "salary": 60000},
    {"priority": 2,"employee_id": 103, "employee_name": "Charlie", "salary": 55000},
    {"priority": 5, "employee_id": 104, "employee_name": "David", "salary": 70000},
    {"priority": 4, "employee_id": 105, "employee_name": "Eve", "salary": 80000}
]
print("\nBefore Merge Sort:")
for entry in payroll_entries:
    print(f"priority: {entry['priority']}, employee_id: {entry['employee_id']}, employee_name: {entry['employee_name']}, salary: {entry['salary']}")

sorted_payroll = merge_sort(payroll_entries, 'priority')

print("\nAfter Merge Sort:")
for entry in sorted_payroll:
    print(f"priority: {entry['priority']}, employee_id: {entry['employee_id']}, employee_name: {entry['employee_name']}, salary: {entry['salary']}")
