# Merge Sort to sort based on priority
def merge_sort(data, key):
    # Base case: if the list is a single element or empty
    if len(data) <= 1:
        return data

    # Find the middle point
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Recursively split and merge
    left_sorted = merge_sort(left, key)
    right_sorted = merge_sort(right, key)

    # Merge the sorted lists
    return merge(left_sorted, right_sorted, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0

    # Compare elements from both lists and merge them
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from left or right
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Sample data (before merge sort)
payroll_entries = [
    { "priority": 3, "employee_id": 101, "employee_name": "Alice", "salary": 50000},
    {"priority": 1, "employee_id": 102, "employee_name": "Bob", "salary": 60000},
    {"priority": 2,"employee_id": 103, "employee_name": "Charlie", "salary": 55000},
    {"priority": 5, "employee_id": 104, "employee_name": "David", "salary": 70000},
    {"priority": 4, "employee_id": 105, "employee_name": "Eve", "salary": 80000}
]

# Output before merge sort
print("\nBefore Merge Sort:")
for entry in payroll_entries:
    print(f"priority: {entry['priority']}, employee_id: {entry['employee_id']}, employee_name: {entry['employee_name']}, salary: {entry['salary']}")

# Sort the payroll entries based on priority
sorted_payroll = merge_sort(payroll_entries, 'priority')

# Output after merge sort (no braces in the output)
print("\nAfter Merge Sort:")
for entry in sorted_payroll:
    print(f"priority: {entry['priority']}, employee_id: {entry['employee_id']}, employee_name: {entry['employee_name']}, salary: {entry['salary']}")
