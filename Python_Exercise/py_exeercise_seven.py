breath = int(input("enter: "))


def find_length(breath):
    length = 6 * breath
    # print(length)
    return length


def find_height(length):
    height = 3 * length
    # print(length)
    # print(height)
    return height


def volume_area(length, breath, height):
    volume = length * breath * height
    # print(find_length(breath), find_height(find_length(breath)))
    return volume


print(find_length(breath), find_height(find_length(breath)), volume_area(find_length(breath), breath, find_height(find_length(breath))))
