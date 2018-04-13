from dish_name import dishName

dishes_string = input('What would you like? ')
#dishes_string = 'ham, spam, eggs, eggs, sausage, meatballs, spam, spam'
dish_list = []

for dish in dishes_string.title().split(','):
    dish_list.append(dish.strip())

menu = set(dish_list)

for dish1 in menu:
    print(dishName(dish1).prepare_for_print())

