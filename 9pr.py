#Menu - объект; 
#одномерный массив строк фиксированной длины - объект Yozh   +
#строка [i]    +
#вы вышли за предел массива!    +
#a[i]+b[i]; a[j]+b[j]; =c 
#a || b
#print(a[i])  print(a)    +

class Menu:
    def __init__(self):
        self.__vibor = 0 
        while True:
            print("задать массив строк - 1")
            print("изменить массив - 2") 
            print("поэлементная конкатенация массивов - 3") 
            print("слияние массивов - 4") 
            print("вывести элемент массива на печать - 5") 
            print("вывести массив на печать - 6") 
            print("выйти из программы - 0") 
            self.__vibor = int(input(">> "))
            if self.__vibor == 0:
                break
            elif self.__vibor == 1:
                length = int(input("количество строк в массиве: "))
                self.A = Yozh(length)
                i=0
                for i in range(length):
                    #str_length = int(input(""))
                    q = input("введите строку (прекратить - !)  ")
                    if q=='!':
                        break
                    else:
                        self.A.__setitem__(i, q) 
                        i=i+1
                pass
            elif self.__vibor == 2:
                ind = int(input("введите индекс "))
                ind = ind - 1
                zna = input("введите строку ")
                self.A.__setitem__(ind, zna) 
            elif self.__vibor == 3:
                pass
            elif self.__vibor == 4:
                pass
            elif self.__vibor == 5:
                ind = int(input("введите индекс "))
                ind = ind - 1
                self.A.print(ind) 
            elif self.__vibor == 6:
                self.A.print_array()
            else:
                print("вы не то ввели")
            print()

class YozhException(Exception):
    pass

class Yozh:
    """описание класса для определения одномерных массивов строк фиксированной длины"""
 
    def __init__(self, length: int, str_length=35):
        
        #length: длина массива
        #str_length: длина строки в массиве
        
        if not isinstance(length, int):   #явл ли объектом класса  
            raise YozhException()
        if not isinstance(str_length, int):   #явл ли объектом класса 
            raise YozhException()   
        self.__length = length
        self.__str_length = str_length 
        self.__yozhiki = ['' for _ in range(length)]
 
    def __setitem__(self, index: int, value: str):
        if not isinstance(index, int):
            raise YozhException('int != {}'.format(type(index)))
        if not isinstance(value, str):
            raise YozhException('')
        if len(value) > self.__str_length:
            raise YozhException('строка слишком длинная')       
        if (self.__check_overflow(index)):
            self.__yozhiki[index] = value
 
    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise YozhException('int != {}'.format(type(index)))
        if (self.__check_overflow(index)):
            return self.__yozhiki[index]
 
    def __check_overflow(self, index: int):
        if not (0 <= index < len(self.__yozhiki)):
            #raise YozhException('выход за границы массива')
            #pass
            print("выход за границы массива")
            return 0
        else:
            return 1
    
    def print(self, index: int):
        """печать (вывод на экран) элементов массива"""
        #print(self[index])
        print(self.__getitem__(index))
 
    def print_array(self):
        """печать (вывод на экран) всего массива"""
        print(self)
 
    def __str__(self):
        return ' '.join(self.__yozhiki)

    def add(self, par):
        print(self.__yozhiki)
        print(self.__length)
        if '' in self.__yozhiki: 
            self.__yozhiki.append(par)
        else:
            print(f"{par} не был записан - превышена длина.")

'''
arr = Yozh(3)
arr[0] = 'POSIES!'
# arr[3] = 'POSIES!3'
print(arr[0])
'''
me = Menu()

