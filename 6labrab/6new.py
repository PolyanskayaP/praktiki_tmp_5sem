import os
import tkinter as tk #ccccccc
from tkinter import filedialog #ccccccc
class Tovar:
    def __init__(self, _name, _shop, _price, _kolvo):
        self.name = _name
        self.shop = _shop
        self.price = _price
        self.kolvo = _kolvo 

    def getName(self):
        return self.name
    def getShop(self):
        return self.shop
    def getPrice(self):
        return self.price
    def getKolvo(self):
        return self.kolvo 
    
    def setName(self,_name):
        self.name = _name
    def setShop(self,_shop):
        self.shop = _shop
    def setPrice(self,_price):
        self.price = _price
    def setKolvo(self,_kolvo):
        self.kolvo = _kolvo

class Menu: #сохранениеААААААА  #методыпереименоватть #tov-name   
    def __init__(self):  
        #root = tk.Tk()
        #root.withdraw()
        #print("БАЗА ДАННЫХ МАГАЗИНА")
        self.list = []
        f = True 
        while f:
            print("Новый файл - 1")
            print("Существующий файл - 2")
            try:
                m = int(input("Введите цифру "))
                if m == 1 or m == 2:
                    f = False
            except ValueError:
                #self.clear()
                continue
        if m == 2:
            #print("Выберите файл в открывшемся диалоговом окне...")
            #file = filedialog.askopenfile(initialdir =os.getcwd(), title = "Выберите файл", filetypes=(("Text Files", "*.txt"),))
            
            #spisok failov!!!!!!!
            file_name = input("введите название файла: ")
            with open(file_name, 'r') as file:
                if file != None:
                    try:
                        arr = file.read().split('\n')
                        for i in arr:
                            temp = i.split(',')
                            name = temp[0]
                            shop = temp[1]
                            price = temp[2]
                            kolvo = temp[3]
                            self.list.append(Tovar(name,shop,price,kolvo))
                    except:
                            print("Ошибка при обработке файла...")
                            #self.clear()
                            #self.reset()
                else:
                    print("Ошибка при открытии файла...")
                    #self.clear()
                    #self.reset()
                return

    def save(self):
        if not len(self.list):
            print("Нет данных ")
            return
        listvr = []
        for i in self.list:
            name = i.getName()
            shop = i.getShop()
            price = i.getPrice()
            kolvo = i.getKolvo()
            tempString = ','.join([name,shop,price,kolvo])
            listvr.append(tempString)
        #print("Выберите, как сохранить файл, в открывшемся диалоговом окне...")
      #  file = filedialog.asksaveasfile(defaultextension='.txt')
        file_name = input("введите название файла: ")
        with open(file_name, 'w') as file:
            string = '\n'.join(listvr)
            file.write(string)

    '''def reset(self):
        self.__init__()''' 

    '''def clear(self):
        input("Нажмите ENTER, чтобы продолжить...")
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
    '''
    def navigation(self):        
        print('Информация о товаре - 1')
        print('Добавить товар - 2')
        print('Изменить информацию о товаре - 3')
        print('Вывести товары в отсортированном виде по названию товара - 4')
        print('Вывести товары в отсортированном виде по названию магазина - 5')
        print('Сохранить файл как - 6')
        #print('Закрыть файл - 9')
        #print('Выйти из программы - 0')
        m = int(input('Введите номер пункта:  ')) 
        #if choice == 0:
        #    flag = False
        if (m > 0 and m < 7):
            if m == 1:
                try:
                    self.info_tov(tov=input("Введите название товара: ")) 
                except:
                    print("Такого товара нет ")
                #self.clear()
            if m == 2:
                self.add()
                #self.clear()
            if m == 3:
                self.edit()
                #self.clear()
            if m == 4:
                self.sortirovka_tov()
                #self.clear()
            if m == 5:
                self.sortirovka_magaz()
                #self.clear()
            if m == 6:
                self.save()
                #self.clear()
        else:
            print("неверный номер")
            return 
        #if choice == 9:
        #    self.clear()
        #    self.reset()

    def info_tov(self,**kwargs): 
        if not len(self.list):
            print("Товаров в данном файле нет")
            return
        if 'tow' in kwargs.keys():
            f = 0
            prod_List = []
            for kortej in self.list:
                if kortej.getName() == kwargs['name']:
                    #print("Товар: ",len(prod_List)+1,":")
                    print("Название товара - ", kortej.getName())
                    print("Магазин - ", kortej.getShop())
                    print("Цена - ", kortej.getPrice())
                    print("Количество - ", kortej.getKolvo())
                    print()
                    f = 1
                    prod_List.append(kortej)
            if f == 0:
                print("Такого товара не существует ")
            return prod_List
        else:
            for kortej in self.list:
                print("Название товара - ", kortej.getName())
                print("Магазин - ", kortej.getShop())
                print("Цена - ", kortej.getPrice())
                print("Количество - ", kortej.getKolvo())
                print()
            return

    def add(self,**kwargs):
        name = input("Введите название товара: ")
        shop = input("Введите название магазина: ")        
        while True:
            price = input("Цена в т.р.: ")
            try:
                priceval = int(price)
                price = str(priceval) + ' т.р.' 
                break
            except ValueError:
                print("Значение цены должно быть числовым")
        while True:
            kolvo = input("Количество: ")
            try:
                kolvoVal = int(kolvo)
                while True:
                    zn = input("Укажите количество (шт., г., кг., м., л.):")
                    setzn = {'кг.', 'м.', 'г.', 'л.', 'шт.'}
                    if zn in setzn:
                        break
                    else:
                        print("Неверная единица измерения ")
            except ValueError:
                print("Значение количества должно быть числовым")
            kolvo = str(kolvoVal) + ' ' + zn
            break
        self.list.append(Tovar(name, shop, price, kolvo))
        self.save()

    def edit(self):
        name = input("Название товара: ")
        if name == '': 
            print("Вы ничего не ввели")
            return
        tov_List = self.info_tov(tov=name)
        if tov_List == None:
            return
        choice = 0
        if len(tov_List) > 1:
            while True:
                try:
                    choice = int(input("Введите номер товара:"))
                    break
                except ValueError:
                    continue
        #self.clear()
        try:
            print() #"Выбранный товар:"
            vybtov = tov_List[choice-1]
            print("Название: ", vybtov.getName())
            print("Магазин: ", vybtov.getShop())
            print("Цена: ", vybtov.getPrice())
            print("Кол-во: ", vybtov.getKolvo())
            print()
        except:
            print("Вы неправильно ввели данные ")
            #self.clear()
            self.edit()
        print('Изменить название товара - 1')
        print('Изменить название магазина - 2')
        print('Изменить цену товара - 3')
        print('Изменить количество товара - 4')
        #print('Отмена - 0')
        while True:
            try:
                choice = int(input('Введите номер варианта: '))
                if choice in [1,2,3,4,0]:
                    break
            except ValueError:
                continue
        #if choice == 0:
         #   return 
        if choice == 1:
            name = input("Название товара: ")
            vybtov.setName(name)
        if choice == 2:
            shop = input("Название магазина: ")
            vybtov.setShop(shop)
        if choice == 3:
            while True:
                price = input("Цена в т.р.: ")
                try:
                    priceval = int(price)
                    price = str(priceval) + ' т.р.' 
                    break
                except ValueError:
                    print("Значение цены должно быть числовым")
            vybtov.setPrice(price)
        if choice == 4:
            while True:
                kolvo = input("Количество: ")
                try:
                    kolvoVal = int(kolvo)
                    while True:
                        zn = input("Укажите количество (шт., г., кг., м., л.):")
                        setzn = {'кг.', 'м.', 'г.', 'л.', 'шт.'}
                        if zn in setzn:
                            break
                        else:
                            print("Неверная единица измерения ")
                    kolvo = str(kolvoVal) + ' ' + zn
                    break
                except ValueError:
                    print("Значение количества должно быть числовым ")
            vybtov.setKolvo(kolvo)
        self.save() 

    def sortirovka_magaz(self):
        self.list = sorted(self.list,key=lambda x:x.getShop())
        self.info_tov()
    
    def sortirovka_tov(self):
        self.list = sorted(self.list,key=lambda x:x.getName())
        self.info_tov()
    
    

if __name__=="__main__":
    root = Menu()
    root.navigation()   