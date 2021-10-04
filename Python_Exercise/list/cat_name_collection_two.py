def cat_name_collection_two():
    cat_name_collections = []
    counter = 1
    cat_name = ""

    while cat_name != "stop":
        cat_name = input(f'Enter the name of cat {counter} ')
        cat_name_collections.append(cat_name)
        counter += 1
    cat_name_collections.pop()
    return cat_name_collections


print(cat_name_collection_two())