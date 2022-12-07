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
                data = input("введите цену в тыс.руб: ") #если дробная цена то ошибка наверное ккак ,.
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
        else: #kor  #обратно не забудь \n и ;    не изменяет, а прпсто добавляет
            with open(file_name, 'r') as f:
                butunfile = f.readlines() 
            print(butunfile)  #сделай красивый вывод всего списка
            tov = input("введите название товара, информацию о котором хотите изменить: ")
            izm=ret_info_tov2(file_name, tov)
            izm_str = (f"{izm[0]};{izm[1]};{izm[2]};{izm[3]}")  #если не то ввели? \n стерла
            print(izm_str)

            osh=1
            dat_str = ""
            while osh:
                data = input("введите новое название товара: ")
                data = data.strip()
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and not(data.isnumeric()):
                    dat_str = dat_str + (f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите название магазина: ")
                data = data.strip()
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and not(data.isnumeric()):
                    dat_str = dat_str + (f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите цену в тыс.руб: ") #если дробная цена то ошибка наверное ккак ,.
                data = data.strip()
                data = data.lower()
                if (data != "") and (data != ';') and not(';' in data) and data.isnumeric():
                    dat_str = dat_str + (f"{data};") 
                    osh=0
                else:
                    print("Некорректные данные ")
            osh=1
            while osh:
                data = input("введите кол-во с ед.изм: ")
                data = data.strip()
                data = data.lower()

                if (data != "") and (data != ';') and not(';' in data): #дописать обработку ошибок здесь
                    dat_str = dat_str + (f"{data};\n") 
                    osh=0
                else:
                    print("Некорректные данные ")
            
            with open(file_name, "w") as f:
                for line in butunfile:
                    if line.strip("\n") != izm_str:
                        f.write(line)
                f.write(dat_str)     



def sort_tov_nazv(file_name):
    with open(file_name, '') as f:
        pass 

def ret_info_tov(file_name):  
    with open(file_name, 'r') as f:
        tov = input("введите название товара: ")
        tov = tov.lower() 
        while True:
            s = f.readline()
            if not s: break 
            data = s.split(';') 
            data.pop()
            if data[0]==tov:
                return data 

def ret_info_tov2(file_name, tov):   ########
    with open(file_name, 'r') as f:
        tov = tov.lower() 
        while True:
            s = f.readline()
            if not s: break 
            data = s.split(';') 
            data.pop()
            if data[0]==tov:
                return data 
                
def info_tov(file_name):
    data = ret_info_tov(file_name)
    if data:
        data_form = (f"Товар: {data[0]}\nМагазин: {data[1]}\nЦена: {data[2]} тыс.руб.\nКол-во: {data[3]}\n")
        print(data_form)
    else:
        print("такого товара нет :( ")

def info_tov2(file_name, tov):  #######
    data = ret_info_tov2(file_name, tov)
    if data:
        data_form = (f"Товар: {data[0]}\nМагазин: {data[1]}\nЦена: {data[2]} тыс.руб.\nКол-во: {data[3]}\n")
        print(data_form)
    else:
        print("такого товара нет :( ")

def record_ayn_bask(file_name):
    with open(file_name, '') as f:
        m = int(input(""))

dop_kor(file_name)
#info_tov(file_name)