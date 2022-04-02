def list_maker():
    list_maker = []

    while True:
        print(f"What is the {(len(list_maker) + 1)} item in your list")
        item = input()
        if item == '':
            break
        list_maker = list_maker + [item]
    print('Items from the list are:')
    for index, item in enumerate(list_maker):
        print(f'{index + 1}.  {item}')


