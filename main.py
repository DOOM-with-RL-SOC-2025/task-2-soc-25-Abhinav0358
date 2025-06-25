"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            age= int(input("Age:"))
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branch_list = [int(code.strip()) for code in branchcodes.split(',')]
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5

            salary = input("Salary: ")
            position= input("Position: ")
            # Create a new Engineer with given details.
            engineer = Engineer(name,age,ID,city,branch_list,position,salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            age= int(input("Age:"))
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branch_list = [int(code.strip()) for code in branchcodes.split(',')]
            salary = input("Salary: ")
            position= input("Position: ")
            superior_ID = input("Superior ID: ")
            salesperson = Salesman(name,age,ID,city,branch_list,superior_ID,salary,position)
            sales_roster.append(salesperson)  
            

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = []
                for branch_code in found_employee.branches:
                    if branch_code in branchmap:
                        branch_names.append(branchmap[branch_code]["name"])
                string_branches = ', '.join(branch_names)

                ## ???? what comes here??
                # print(f"Branches: " + ???? )
                print(f"Branches: {string_branches}")
                
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("Enter Employee ID"))
            new_code= int(input("Enter new branch code: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            if found_employee is not None:
                found_employee.migrate_branch(new_code)

            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            position = str(input("Enter new position: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            if found_employee is not None:
                found_employee.promote(position)
            else:
                print("No such employee found")
            # promote employee to next position

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            amount = int(input("Enter increment amount: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            if found_employee is not None:
                found_employee.increment(amount)
            else:
                print("No such employee found")
            # Increment salary of employee.
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            found_employee = None
            for employee in  sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            if found_employee is not None:
                if found_employee.superior is None:
                    print("No superior found")  
                else:
                    print(found_employee.find_superior())
            else:
                print("No such sales employee found")
            # Print superior of the sales employee.
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            found_employee = None
            for employee in  sales_roster:
                if employee.ID == int(ID_E):
                    found_employee = employee
                    break
            if found_employee:
                found_employee.add_superior(ID_S)

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






