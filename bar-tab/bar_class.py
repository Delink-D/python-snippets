class Tab:

    menu ={
        'wine': 200,
        'beer': 250,
        'softDrink': 100,
        'beef': 300,
        'veggie': 150,
        'desert': 120
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax=int(input('input Tax: ')), service=int(input('Service charge: '))):
        tax = (tax/100)*self.total
        service = (service/100)*self.total

        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} Ksh.{self.menu[item]}')

        print(f'{"TOTAL":20} Ksh.{total}')
