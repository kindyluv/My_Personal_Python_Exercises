def pizza_deliveries_three():
    print("Welcome to precious pizza deliveries!")
    pizza_size = input("What size of pizza do want? small, medium and large:  ")
    add_pepperoni = input("Do you want pepperoni? yes or no  ")
    extra_cheese = input("Do you want extra cheese? yes or no  ")

    cost = 0
    if pizza_size == "small":
        cost += 15
        print(f"your pizza bill is {cost}")
    elif pizza_size == "medium":
        cost += 20
        print(f"your pizza bill is {cost}")
    elif pizza_size == "large":
        cost += 25
        print(f"your pizza bill is {cost}")
    else:
        print("no under wetin you want oh")
    if add_pepperoni == "yes":
        if pizza_size == "small":
            cost += 2
            print(f"your final bill is {cost}")
#     else:
#         cost += 3
#         print(f"your final bill is {cost}")
#     if extra_cheese == "yes":
#         cost += 1
#         print(f"your final bill is {cost}")
#     else:
#         print("you too broke go joor")
#
#
# pizza_deliveries_three()
