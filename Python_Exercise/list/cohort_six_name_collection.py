def cohort_six_name_collection():
    cohort_six = []
    counter = 1

    six_input = ""
    while six_input != "stop":
        six_input = input(f'Enter the names of cohort six natives {counter} ')
        cohort_six.append(six_input)
        counter += 1
        cohort_six.pop()
    return cohort_six


print(cohort_six_name_collection())