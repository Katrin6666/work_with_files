from pprint import pprint

with open('recipes.txt', encoding='utf-8') as menu:

    cook_book = {}
    for line in menu:
        number = int(menu.readline())
        lines = []
        for item in range(number):
            data = menu.readline().strip().split('|')
            data2 = {}
            data2['ingredient_name'] = data[0]
            data2['quantity'] = data[1]
            data2['measure'] = data[2]
            lines.append(data2)
        cook_book[line.strip()] = lines
        menu.readline()
pprint(cook_book)

# 'ingredient_name'
# 'quantity'
# 'measure'