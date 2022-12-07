import os
import tkinter as tk
from tkinter import filedialog
class Goods:
    def __init__(self, _name, _shop, _cost, _amount):
        self.name = _name
        self.shop = _shop
        self.cost = _cost
        self.amount = _amount 

    def getName(self):
        return self.name
    def getShop(self):
        return self.shop
    def getCost(self):
        return self.cost
    def getAmount(self):
        return self.amount
    
    def setName(self,_name):
        self.name = _name
    def setShop(self,_shop):
        self.shop = _shop
    def setCost(self,_cost):
        self.cost = _cost
    def setAmount(self,_amount):
        self.amount = _amount

class Menu:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        print("БАЗА ДАННЫХ МАГАЗИНА")
        self.list = []
        flag = True
        while flag:
            print("[1] Новый файл")
            print("[2] Открыть уже существующий файл")
            try:
                choice = int(input("> "))
                if choice == 1 or choice == 2:
                    flag = False
            except ValueError:
                self.clear()
                continue
        if choice == 2:
            print("Выберите файл в открывшемся диалоговом окне...")
            file = filedialog.askopenfile(initialdir =os.getcwd(), title = "Выберите файл", filetypes=(("Text Files", "*.txt"),))
            if file != None:
                try:
                    arr = file.read().split('\n')
                    for i in arr:
                        temp = i.split(',')
                        name = temp[0]
                        shop = temp[1]
                        cost = temp[2]
                        amount = temp[3]
                        self.list.append(Goods(name,shop,cost,amount))
                except:
                        print("Ошибка при обработке файла...")
                        self.clear()
                        self.reset()
            else:
                print("Ошибка при открытии файла...")
                self.clear()
                self.reset()
            return

    def reset(self):
        self.__init__()

    def clear(self):
        input("Нажмите ENTER, чтобы продолжить...")
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')

    def view(self,**kwargs):
        if not len(self.list):
            print("База данных пустая...")
            return
        if 'name' in kwargs.keys():
            flag = 0
            goodsList = []
            for i in self.list:
                if i.getName() == kwargs['name']:
                    print("Товар ",len(goodsList)+1,":")
                    print("Название товара:", i.getName())
                    print("Продаётся в магазине:", i.getShop())
                    print("Цена товара:", i.getCost())
                    print("Количество товара:", i.getAmount())
                    print()
                    flag = 1
                    goodsList.append(i)
            if flag == 0:
                print("Ничего не найдено...")
            return goodsList
        else:
            for i in self.list:
                print("Название товара:", i.getName())
                print("Продаётся в магазине:", i.getShop())
                print("Цена товара:", i.getCost())
                print("Количество товара:", i.getAmount())
                print()
            return

    def add(self,**kwargs):
        name = input("Название товара: ")
        shop = input("Название магазина: ")        
        while True:
            cost = input("Цена: ")
            try:
                costval = int(cost)
                while True:
                    value = input("Укажите цену (р., т.р., $):")
                    valid = {'р.','т.р.', '$'}
                    if value in valid:
                        break
                    else:
                        print("Мы такую валюту не знаем...")
                cost = str(costval) + ' ' + value 
                break
            except ValueError:
                print("Укажите значение цены в числовом виде...")
        while True:
            amount = input("Количество: ")
            try:
                amountVal = int(amount)
                while True:
                    value = input("Укажите количество (кг, г, шт.):")
                    valid = {'кг','г', 'шт.'}
                    if value in valid:
                        break
                    else:
                        print("В таких единицах не считаем...")
            except ValueError:
                print("Укажите значение количества в числовом виде...")
            amount = str(amountVal) + ' ' + value
            break
        self.list.append(Goods(name,shop,cost,amount))

    def edit(self):
        name=input("Название товара (ENTER чтобы выйти): ")
        if name == '':
            return
        goodsList = self.view(name=name)
        if goodsList == None:
            return
        choice = 0
        if len(goodsList) > 1:
            while True:
                try:
                    choice = int(input("Введите номер товара:"))
                    break
                except ValueError:
                    continue
        self.clear()
        try:
            print("Выбранный товар:")
            k = goodsList[choice-1]
            print("Название товара:", k.getName())
            print("Продаётся в магазине:", k.getShop())
            print("Цена товара:", k.getCost())
            print("Количество товара:", k.getAmount())
            print()
        except:
            print("Ошибка при вводе данных...")
            self.clear()
            self.edit()
        print('[1] Изменить название товара')
        print('[2] Изменить название магазина')
        print('[3] Изменить цену товара')
        print('[4] Изменить количество товара')
        print('[0] Отмена')
        while True:
            try:
                choice = int(input('>'))
                if choice in [1,2,3,4,0]:
                    break
            except ValueError:
                continue
        if choice == 0:
            return
        if choice == 1:
            name = input("Название товара: ")
            k.setName(name)
        if choice == 2:
            shop = input("Название магазина: ")
            k.setShop(shop)
        if choice == 3:
            while True:
                cost = input("Цена: ")
                try:
                    costval = int(cost)
                    while True:
                        value = input("Укажите цену (р., т.р., $):")
                        valid = {'р','т.р.', '$'}
                        if value in valid:
                            break
                        else:
                            print("Мы такую валюту не знаем...")
                    cost = str(costval) + ' ' + value 
                    break
                except ValueError:
                    print("Укажите значение цены в числовом виде...")
            k.setCost(cost)
        if choice == 4:
            while True:
                amount = input("Количество: ")
                try:
                    amountVal = int(amount)
                    while True:
                        value = input("Укажите количество (кг, г, шт.):")
                        valid = {'кг','г', 'шт.'}
                        if value in valid:
                            break
                        else:
                            print("В таких единицах не считаем...")
                    amount = str(amountVal) + ' ' + value
                    break
                except ValueError:
                    print("Укажите значение количества в числовом виде...")
            k.setAmount(amount)

    def sortByShop(self):
        self.list = sorted(self.list,key=lambda x:x.getShop())
        self.view()
    
    def sortAlphabetic(self):
        self.list = sorted(self.list,key=lambda x:x.getName())
        self.view()
    
    def save(self):
        if not len(self.list):
            print("Нечего сохранять...")
            return
        tempArr = []
        for i in self.list:
            name = i.getName()
            shop = i.getShop()
            cost = i.getCost()
            amount = i.getAmount()
            tempString = ','.join([name,shop,cost,amount])
            tempArr.append(tempString)
        print("Выберите, как сохранить файл, в открывшемся диалоговом окне...")
        file = filedialog.asksaveasfile(defaultextension='.txt')
        string = '\n'.join(tempArr)
        file.write(string)

    def root(self):
        flag = True
        while flag:
            print('[1] Вывести сведения о товаре')
            print('[2] Добавить товар')
            print('[3] Изменить сведения о товаре')
            print('[4] Вывести все товары в алфавитном порядке')
            print('[5] Вывести товары по названию магазина')
            print('[8] Сохранить файл как...')
            print('[9] Закрыть файл')
            print('[0] Выйти из программы')
            try:
                choice = int(input('> '))
            except ValueError:
                continue
            if choice == 0:
                flag = False
            if choice == 1:
                try:
                    self.view(name=input("Название товара: "))
                except:
                    print("Ошибка при вводе данных...")
                self.clear()
            if choice == 2:
                self.add()
                self.clear()
            if choice == 3:
                self.edit()
                self.clear()
            if choice == 4:
                self.sortAlphabetic()
                self.clear()
            if choice == 5:
                self.sortByShop()
                self.clear()
            if choice == 8:
                self.save()
                self.clear()
            if choice == 9:
                self.clear()
                self.reset()


if __name__=="__main__":
    root = Menu()
    root.root()