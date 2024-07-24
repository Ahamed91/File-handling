# File-handling - Employee Management System

This Python script manages employee records, allowing you to add, delete, and save employee details in a CSV file.

## Features
Load Employee Data: Reads employee details from a CSV file.  
Add Employee: Add new employees to the list.  
Delete Employee: Remove employees by their username.  
Save Data: Save the current employee list to a CSV file.  
Interactive Menu: Provides a user-friendly interface to manage employees.  

## Prerequisites
Python 3.x  
CSV file named "employee_list_report.csv" (optional, script will handle if file is not found)

# Script Overview
## Functions
### csv_to_list()
Loads employee data from employee_list_report.csv.  
Returns an empty list if the file is not found. 

### add_employee(employee_list)
Prompts the user for employee details (full name, username, department).  
Adds the new employee to the list.  

### delete_employee(employee_list)
Prompts the user for the username of the employee to delete.  
Removes the employee from the list if found.  

### append_employee(employee_list)
Adds a new employee to the list by calling add_employee().  

### employees_report(employee_list)  
Saves the employee list to employee_list_report.csv.  

### manage_employee()
Provides an interactive menu for managing employees.  

## Usage
Load Existing Data: Automatically loads data from employee_list_report.csv if the file exists.  
Add an Employee: Select option 1 from the menu to add a new employee. Enter the details when prompted.  
Delete an Employee: Select option 2 from the menu to delete an employee. Enter the username of the employee to remove.  
Save Data: Select option 3 to save the current list of employees to the CSV file.  
Exit: Select option 4 to exit the script.  