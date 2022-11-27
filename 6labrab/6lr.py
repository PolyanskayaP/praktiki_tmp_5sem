#9вар  список товаров; название-назвмагаз-стоимвтыс-колвоседизмер
#menu = int(input("1- 2- 3- 4-"))
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
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and not(data.isnumeric()):
                    f.write(f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите название магазина: ")
                data = data.strip()
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and not(data.isnumeric()):
                    f.write(f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите цену в тыс.руб: ")
                data = data.strip()
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and data.isnumeric():
                    f.write(f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите кол-во с ед.изм: ")
                data = data.strip()
                data = data.lower()

                if (data != "") and (data != ';') and not(';' in data): #дописать обработку ошибок здесь
                    f.write(f"{data};\n") 
                    osh=0
                else:
                    print("Некорректные данные ")
        else:
            pass 

def sort_tov_nazv(file_name):
    with open(file_name, '') as f:
        pass 

def info_tov(file_name):  #,tov
    with open(file_name, 'r') as f:
        tov = input("введите название нужного товара: ")
        tov = tov.lower() 
        while True:
            s = f.readline()
            if not s: break 
            data = s.split(';') 
            if data[0]==tov:
                print(f"Товар: {data[0]}\nМагазин: {data[1]}\nЦена: {data[2]}тыс.руб.\nКол-во: {data[3]}\n")


def record_ayn_bask(file_name):
    with open(file_name, '') as f:
        m = int(input(""))

#dop_kor(file_name)
info_tov(file_name)