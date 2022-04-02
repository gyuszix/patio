list = ['1', ',', ' ', '2', ',', ' ', '3']

for index, item in enumerate(list):
    print(index, item)
    del item
    print(list)
#    if item == ' ' or ',':
#        del item


