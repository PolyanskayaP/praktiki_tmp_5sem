#9вар  список товаров; название-назвмагаз-стоимвтыс-колвоседизмер
menu = int(input("1- 2- 3- 4-"))
file_name="bd_tov.txt"
f = open(file_name,'a') 
f.close()

def dop_kor(file_name):
    with open(file_name, 'a') as f: 
        m = int(input("1-дополнить, 0-корректировать: "))
        if m:
            osh=1
            while osh:
                data = input("введите название товара: ")
                data = data.strip()
                if (data != "") and (data != ';'):
                    f.write(f"{data};") 
                    osh=0
            osh=1
            while osh:
                data = input("введите название магазина: ")
                data = data.strip()
                if (data != "") and (data != ';'):
                    f.write(f"{data};") 
                    osh=0
            osh=1
            while osh:
                data = input("введите цену в тыс.руб: ")
                data = data.strip()
                if (data != "") and (data != ';'):
                    f.write(f"{data};") 
                    osh=0
            osh=1
            while osh:
                data = input("введите кол-во с ед.изм: ")
                data = data.strip()
                if (data != "") and (data != ';'):
                    f.write(f"{data};\n") 
                    osh=0
        else:
            pass 

def sort_tov_nazv(file_name):
    with open(file_name, '') as f:
        pass 

def info_tov(file_name):  #,tov
    with open(file_name, '') as f:
        pass 

def record_ayn_bask(file_name):
    with open(file_name, '') as f:
        pass 

dop_kor(file_name)