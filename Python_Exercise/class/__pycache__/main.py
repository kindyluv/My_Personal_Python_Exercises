# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/r
# import item
from item import Item
from item import Cart

# cart_owner_name = "default"////
cart = Cart("default")


def set_up_cart():
    global cart
    cart_owner_name = input("what is the owner's name: ")
    cart = Cart(cart_owner_name)


def add_items_to_cart():
    add_more_items = "yes"
    while add_more_items.lower() == "yes":
        # add_item_to_cart()
        add_item_to_cart()
        add_more_items = input("Anything else? \n")
        print(add_more_items)


def add_item_to_cart():
    item_name = input("What item did" + cart.owner_name + "purchased \n")
    item_price = float(input("How much does the " + item_name + "cost \n"))
    item_quantity = int(input("how many " + item_name + " " + cart.owner_name + "buy \n"))
    new_item = Item(item_name, item_price, item_quantity)
    cart.add(new_item)


def display_invoice():
    print(cart)
    print(str(cart.calculate_total_price()))
    print(str(cart.calculate_vat_of(7.5)))


if __name__ == '__main__':
    set_up_cart()
    add_items_to_cart()
    display_invoice()
