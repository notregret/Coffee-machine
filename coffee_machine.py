class Coffemashine:
    def __init__(self, water, milk, coffee, money, cups):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.cups = cups

    def machine(self):
        vi_ = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if vi_.isdigit():
            vi_ = int(vi_)
        if vi_ == 1:
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
            elif self.water < 250:
                print('Sorry, not enough water')
            elif self.coffee < 16:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
        elif vi_ == 2:
            if self.water >= 350 and self.coffee >= 20 \
                    and self.cups >= 1 and self.milk >= 75:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
            elif self.water < 350:
                print('Sorry, not enough water')
            elif self.coffee < 20:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            elif self.milk < 75:
                print('Sorry, not enough milk')
        elif vi_ == 3:
            if self.water >= 200 and self.coffee >= 12 \
                    and self.cups >= 1 and self.milk >= 100:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
            elif self.water < 200:
                print('Sorry, not enough water')
            elif self.coffee < 12:
                print('Sorry, not enough beans')
            elif self.cups < 1:
                print('Sorry, not enough cups')
            elif self.milk < 100:
                print('Sorry, not enough milk')
        else:
            return 0
            print()


    def fill(self):
        water_ = int(input("Write how many ml of water do you want to add:\n"))
        milk_ = int(input("Write how many ml of milk do you want to add:\n"))
        coffee_ = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups_ = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.water += water_
        self.milk += milk_
        self.coffee += coffee_
        self.cups += cups_

    def take(self):
        if self.money > 0:
            print("I gave you", self.money)
            self.money = 0
        else:
            print("I have no money")

    def result(self):
        print("""
    The coffee machine has:\n""",
              self.water, "of water\n",
              self.milk, """of milk\n""",
              self.coffee, """of coffee beans\n""",
              self.cups, """of disposable cups\n""",
              self.money, """of money""")

    def do_it(self):
        while True:
            act = input('Write action (buy, fill, take, remaining, exit): ')
            if act == 'buy':
                self.machine()
            elif act == 'fill':
                self.fill()
            elif act == 'take':
                self.take()
            elif act == 'remaining':
                self.result()
            else:
                break


coffee = Coffemashine(400, 540, 120, 550, 9)
coffee.do_it()