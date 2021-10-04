from list.employee_department_list import create_new_employee_department
from list.employee_list import create_new_employee_name_database


def print_out():
    for full_name in create_new_employee_name_database():
        print(full_name, end="")

    for department in create_new_employee_department():
        print(department, end="")


print_out()