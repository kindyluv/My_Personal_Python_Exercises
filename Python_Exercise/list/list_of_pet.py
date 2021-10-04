def create_list_of_pet():
    my_pet = []

    pet = " "
    while pet != " ":
        pet_input = input('Enter names of pets \n')
        my_pet.append(pet_input)

    return my_pet