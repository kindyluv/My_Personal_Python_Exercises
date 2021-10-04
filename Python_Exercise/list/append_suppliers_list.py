def append_suppliers_list():
    suppliers = []
    counter = 1
    supply = ""
    while supply != "stop":
        supply = input(f'Enter first name and last name of suppliers {counter} \n')
        suppliers.append(supply)
        counter += 1
        suppliers.pop()
    return suppliers


append_suppliers_list()