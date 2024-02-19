

# Setting up a simple combat roll turn based game. going to play around with objects and classes

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.coins = 5
        self.inventory = {}
        self.__level = 1
        self.__exp = 0
        self.__math_exp = 0
        self.__max_hp = 100 + (100 * (self.__level - 1))

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.__level

    def pay_coin_charge(self, charge):
        if self.coins < charge:
            print('You do not have enough coins to play the math quiz.')
            print('You need to go to work and earn some coins.')
            self.coins = 1
        else:
            self.coins -= charge

    def give_math_experience(self, exp):
        self.__math_exp += exp
        if self.__math_exp >= 100:
            self.__level += 1
            self.__math_exp = 0
            print('Congratulations! You have leveled up.')
            print('You are now level: ', self.__level)

    def print_all_data(self):
        print('Name: ', self.name)
        print('Level: ', self.__level)
        print('Experience: ', self.__exp)
        print('Coins: ', self.coins)
        print('Inventory: ', self.inventory)

class Store:
    def __init__(self, player):
        self.items = {
            'sword': 10,
            'shield': 5,
            'potion': 5,
            'meal': 3
        }
        self.player = player

    def show_items(self):
        print('Welcome to the store. Here are the items available for purchase:')
        for item, cost in self.items.items():
            print(f'{item}: {cost} coins')

    def buy_item(self, item):
        # do they have enough coins?
        if self.player.coins < self.items[item]:
            print('You do not have enough coins to buy this item.')
            print('You need to go to work and earn some coins.')
        elif item in self.player.inventory:
            print('You already have this item.')
        elif item in self.items:
            self.player.coins -= self.items[item]
            self.player.inventory[item] = 1
            print('You have purchased a ', item)
        else:
            print('That item is not available for purchase.')
class Math_Quiz:
    def __init__(self, player):
        self.data = []
        self.player = player

    def ask_question(self):
        level = self.player.get_level()
        self.player.pay_coin_charge(1)

        print('player level is: ', level)
        print('player coins: ', self.player.coins)
        
        num1 = random.randint(1, 10*level)
        num2 = random.randint(1, 10*level)

        answer = num1 + num2

        question = f'What is {num1} + {num2}?'
        print(question)
        response = int(input('Enter your answer: '))
        if response == answer:
            print('Correct! You have earned 5 coins.')
            self.player.coins += (5*level)
            self.player.give_math_experience(1)
        else:
            print('Incorrect. The correct answer is: ', answer)

    

    

if __name__ == '__main__':
    
    
    
    #print('Well met, traveler! Welcome to a simple adventure.')
    #print('Let us begin...')
    #print('How should we address you?')
    #name = input('Enter your name and please press enter: ')

    name = 'Player1'
        

    # Create a player object
    player = Player(name)

    """
    print(f'Welcome, {player.get_name()}! Let us begin our journey.')
    print('because this is for school, we are going to have a way to use your brain.')
    print('you can go to work and earn money.')
    print('you get money when you get a correct answer')
    print('it costs one coin to play the math quiz')
    print('a correct answer will give you 5 coins')
    """
    
    math_quiz = Math_Quiz(player)

    math_quiz.ask_question()

    player.print_all_data()

    print('now that you have a couple of coins you can go to the store and buy some items.')
    store = Store(player)
    store.show_items()
    store.buy_item('meal')
    player.print_all_data()

    print('now that you have purchased a meal, you can go home to rest')

    home  = Home(player)
    home.rest()
    
