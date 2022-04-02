list = [1,2,3]


def append_list():
    list = [1, 2, 3]
    list.append(1323)
    print(list)


def insert_list():
    list = [1, 2, 3]
    list.insert(3, 4)
    print(list)


def remove_list():
    list = [1, 2, 3]
    list.remove(2)    # doesn't remove the index # but rather the value of the item
    print(list)


def del_list():
    list = [1, 2, 3]
    del list[0]   # doesn't remove the index but rather the value of the item
    print(list)


list_1 = [1]
list_2 = [2]
list_3 = [list_1, list_2]
print(type(list_3))

tuple_1 = (1,)
tuple_2 = (2,)
tuple_3 = (tuple_1, tuple_2)
print(type(tuple_3))




