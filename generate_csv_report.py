#!/usr/bin/python3

import csv 

def csv_to_list():
    employee_list = []
    try:
        with open("employee_list_report.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_list.append(row)
        print("\nList update succesfull!")
    except:
        print("\nfile not found! Starting with an empty list")
    return employee_list

def add_employee(employee_list):
    employee ={}
    employee['full_name'] = input("Enter Full name: ")
    employee['user_name'] = input("Enter User name: ")
    employee['department'] = input("Enter Department: ")
    employee_list.append(employee)
    print("\nEmployee has been succesfully added!")

def delete_employee(employee_list):
    delete_employee = input("Enter username of the employee: ")
    for employee in employee_list:
        if employee['user_name'] == delete_employee:
            employee_list.remove(employee)
            print("\nEmployee deleted succesfully!")
            return 
    print("\nUser name not found!")

def append_employee(employee_list):
    add_employee(employee_list)

def employees_report(employee_list):
    with open("employee_list_report.csv", 'w') as file:
        keys = employee_list[0].keys() if employee_list else ['full_name', 'user_name', 'department']
        writer = csv.DictWriter(file, fieldnames= keys)
        writer.writeheader()
        writer.writerows(employee_list)
    print("\nEmployee details written succesfully!")


def manage_employee():
    employee_list = csv_to_list()
    while True:
        print("\nOptions:")
        print("1. Add an employee")
        print("2. Delete employee")
        print("3. Update file")
        print("4. exit")
        choice = input("\nEnter your choice: ")

        if choice == '1' and not employee_list:
            add_employee(employee_list)
        elif choice == '1':
            append_employee(employee_list)
        elif choice == '2':
            delete_employee(employee_list)
        elif choice == '3':
            employees_report(employee_list)
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Try again")


if __name__ == "__main__":
    manage_employee()
