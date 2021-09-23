class Item:

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def calculate_total(self):
        return self.__price * self.__quantity

    def __str__(self):
        return self.__name + "\t\t\t" + str(self.__price) + "\t\t" + str(self.__quantity) + "\t\t" + str(
            self.calculate_total())


class Cart:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    # def add(self, item_name, item_price, item_quantity):
    #     item = Item(item_name, item_price, item_quantity)
    #     self.items.append(item)

    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += item.calculate_total()
        return total

    def __str__(self):
        string_to_return = ""
        for item in self.items:
            string_to_return += item.__str__() + "\n"
        return string_to_return

    def calculate_vat_of(self, percentage):
        return self.calculate_total_price()*(percentage/100.0)
