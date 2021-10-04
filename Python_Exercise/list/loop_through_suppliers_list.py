from list.append_suppliers_list import append_suppliers_list


def loop_through_suppliers_list():
    suppliers = append_suppliers_list()
    for names in range(len(suppliers)):
        print('index ' + str(names) + 'in suppliers is: ' + suppliers[names])