
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


def add_employee():
    employees = load_data(EMPLOYEE_FILE)

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    employee = {
        "employee_id": emp_id,
        "name": name,
        "total_leaves": 20
    }

    employees.append(employee)
    save_data(EMPLOYEE_FILE, employees)

    print("Employee added successfully!")


def view_employees():
    employees = load_data(EMPLOYEE_FILE)

    if not employees:
        print("No employees found.")
        return

    for emp in employees:
        print(emp)


def apply_leave():
    leaves = load_data(LEAVE_FILE)
    employees = load_data(EMPLOYEE_FILE)

    emp_id = input("Enter Employee ID: ")

    employee_exists = any(
        emp["employee_id"] == emp_id
        for emp in employees
    )

    if not employee_exists:
        print("Employee ID not found!")
        return

    try:
        days = int(input("Enter number of leave days: "))

        if days<=0:
            print("Leave days must be greater than zero.")
            return
        
    except ValueError:
        print("Please enter a valid number.")
        return

    reason = input("Enter leave reason: ")

    if days>5:
        status = "Pending Manager Approval"
    else:
        status = "Approved"

    leave = {
        "employee_id": emp_id,
        "days": days,
        "reason": reason,
        "status": status
    }

    leaves.append(leave)
    save_data(LEAVE_FILE, leaves)

    print("Leave application submitted!")
    print("Application Status:", status)


def view_leaves():
    leaves = load_data(LEAVE_FILE)

    if not leaves:
        print("No leave applications found.")
        return

    for leave in leaves:
        print(leave)

def show_project_info():
    print("\nEmployee Leave Management System")
    print("Version: 2.0")
    print("Developed using Python")
    print("Version Control: Git and GitHub")

def main():
    while True:
        print("\n===== EMPLOYEE LEAVE MANAGEMENT =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Apply Leave")
        print("4. View Leave Applications")
        print("5. Exit")
        print("6. Project Information")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            apply_leave()
        elif choice == "4":
            view_leaves()
        elif choice == "5":
            print("Exiting application...")
            break
        elif choice == "6":
            show_project_info()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
