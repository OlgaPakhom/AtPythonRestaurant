import random

class dishName(str):
    def __init__(self, dish1):
        self.dish1 = dish1
    
    def dots(self):
        return self.ljust(15, '.')
    
    @staticmethod
    def time():
        return random.randint(0, 100)

    def prepare_for_print(dish1):
        prepared = dishName.dots(dish1) + str(dishName.time()) + ' minutes'
        return prepared
