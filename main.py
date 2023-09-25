from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print(dir(Menu)) #used to see all attributes and methods attached to the class/object
print('------------------------------------------------')
print(dir(MenuItem))
print('------------------------------------------------')
print(dir(CoffeeMaker))
print('------------------------------------------------')
print(dir(MoneyMachine))
print('------------------------------------------------')

ar=[]

print(any(ar))

def make_coffee():
    print('coffee maker report...',CoffeeMaker.report())
    
make_coffee()