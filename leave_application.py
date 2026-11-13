
import json
import os

EMPLOYEE_FILE = "data/employees.json"
LEAVE_FILE = "data/leaves.json"


def load_data(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def apply_leave():
    employees = load_data(EMPLOYEE_FILE)
    leaves = load_data(LEAVE_FILE)

    emp_id = input("Enter Employee ID: ")

    employee = next(
        (emp for emp in employees
         if emp["employee_id"] == emp_id),
        None
    )

    if employee is None:
        print("Employee not found!")
        return

    print("Employee Name:", employee["name"])

    print("Leave Types:")
    print("1. Casual Leave")
    print("2. Sick Leave")
    print("3. Earned Leave")

    leave_choice = input("Select leave type: ")

    leave_types = {
        "1": "Casual Leave",
        "2": "Sick Leave",
        "3": "Earned Leave"
    }

    if leave_choice not in leave_types:
        print("Invalid leave type!")
        return

    try:
        days = int(input("Enter leave days: "))
        if days <= 0:
            print("Days must be greater than zero!")
            return
    except ValueError:
        print("Enter a valid number!")
        return

    reason = input("Enter reason: ")

    if days > 5:
        status = "Manager Approval Required"
    else:
        status = "Leave Can Be Processed"

    leave = {
        "employee_id": emp_id,
        "employee_name": employee["name"],
        "leave_type": leave_types[leave_choice],
        "days": days,
        "reason": reason,
        "status": status
    }

    leaves.append(leave)
    save_data(LEAVE_FILE, leaves)

    print("\nLeave application submitted!")
    print("Status:", status)
