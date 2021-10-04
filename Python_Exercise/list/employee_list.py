def create_new_employee_name_database():
    # global names
    employee_names = []
    emp_input = ""
    while emp_input != " ":
        emp_first_name_input = input('Enter employee first name \n')
        emp_last_name_input = input('Enter employee last name \n')

        employee_names.append(emp_first_name_input)
        employee_names.append(emp_last_name_input)

    return employee_names