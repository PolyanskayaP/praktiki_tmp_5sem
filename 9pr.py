#Menu - объект; 
#одномерный массив строк фиксированной длины - объект Yozh   +
#строка [i]    +
#вы вышли за предел массива!    +
#a[i]+b[i]; a[j]+b[j]; =c   +
#a || b   
#print(a[i])  print(a)    +

class Menu:
    def __init__(self):
        self.__vibor = 0
        self.AA = [] 
        while True:
            print("задать массив строк - 1")
            print("изменить массив - 2") 
            print("поэлементная конкатенация массивов - 3") 
            print("слияние массивов - 4") 
            print("вывести элемент массива на печать - 5") 
            print("вывести массивы на печать - 6") 
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
                self.AA.append(self.A) 
            elif self.__vibor == 2:
                indM = int(input("введите индекс МАССИВА "))
                if indM > len(self.AA):
                    print("неверный индекс массива")
                    break 
                indM = indM - 1
                ind = int(input("введите индекс элемента"))
                ind = ind - 1
                zna = input("введите строку ")
                self.AA[indM].__setitem__(ind, zna) 
            elif self.__vibor == 3:
                indM1 = int(input("введите индекс одного МАССИВА "))
                if indM1 > len(self.AA):
                    print("неверный индекс массива")
                    break 
                indM1 = indM1 - 1

                indM2 = int(input("введите индекс другого МАССИВА "))
                if indM2 > len(self.AA):
                    print("неверный индекс массива")
                    break 
                indM2 = indM2 - 1

                C = self.AA[indM1].poel_concat(self.AA[indM2])
                self.AA.append(C) 
            elif self.__vibor == 4:
                pass
            elif self.__vibor == 5:
                indM = int(input("введите индекс МАССИВА "))
                #indM = indM - 1
                ind = int(input("введите индекс элемента"))
                ind = ind - 1
                #print(len(self.AA))
                if indM <= len(self.AA):
                    indM = indM - 1
                    self.AA[indM].print(ind) 
                else:
                    print("неверный индекс массива")
            elif self.__vibor == 6:
                for B in self.AA:
                    B.print_array()
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
    
    def print(self, index: int):      #печать переделать 
        """печать (вывод на экран) элементов массива"""
        #print(self[index])
        print(self.__getitem__(index))
 
    def print_array(self):
        """печать (вывод на экран) всего массива"""
        print(self)
 
    def __str__(self):
        return ' '.join(self.__yozhiki)

    def poel_concat(self, B: 'Yozh'):
        lenA = self.__length 
        lenB = B.__length
        n = min(lenA, lenB)
        C = Yozh(n)
        for i in range(n):
            stro = self.__getitem__(i) + B.__getitem__(i)
            C.__setitem__(i, stro)
        return C 

    def sliyan(self, B: 'Yozh'):
        pass 

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

