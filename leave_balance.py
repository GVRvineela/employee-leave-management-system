
import json
import os

EMPLOYEE_FILE = "data/employees.json"
LEAVE_FILE = "data/leaves.json"


def load_data(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)


def display_leave_balance():
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

    total_leave = employee.get("total_leaves", 20)

    used_leave = sum(
        leave["days"]
        for leave in leaves
        if leave["employee_id"] == emp_id
        and leave["status"] == "Approved"
    )

    remaining_leave = total_leave - used_leave

    print("\n===== LEAVE BALANCE =====")
    print("Employee:", employee["name"])
    print("Total Leave:", total_leave)
    print("Used Leave:", used_leave)
    print("Remaining Leave:", remaining_leave)
