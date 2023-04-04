<<<<<<< Updated upstream
from tkinter import *

                                                             # Алгоритм автоматически определяет на вводе римские или арабские цифры.
def perivod():
    a = entry.get()
    if a.count('1') >= 1 or a.count('2') >= 1 or a.count('3') >= 1 or a.count('4') >= 1 or a.count('5') >= 1 or a.count('6') >= 1 or a.count('7') >= 1 or a.count('8') >= 1 or a.count('9') >= 1 or a.count('0') >= 1 :
        arabic_zifra = int(entry.get())
        rom_zifra = 'I' * arabic_zifra
        rom_zifra = rom_zifra.replace('IIIII', 'V')
        rom_zifra = rom_zifra.replace('VV', 'X')         # Римская цифра получается путём замены от меньших значений, к большим.
        rom_zifra = rom_zifra.replace('XXXXX', 'L')
        rom_zifra = rom_zifra.replace('LL', 'C')
        rom_zifra = rom_zifra.replace('CCCCC', 'D')
        rom_zifra = rom_zifra.replace('DD', 'M')
        rom_zifra = rom_zifra.replace('DCCCC', 'CM')
        rom_zifra = rom_zifra.replace('CCCC', 'CD')
        rom_zifra = rom_zifra.replace('LXXXX', 'XC')
        rom_zifra = rom_zifra.replace('XXXX', 'XL') 
        rom_zifra = rom_zifra.replace('VIIII', 'IX')
        rom_zifra = rom_zifra.replace('IIII', 'IV') 
        print(rom_zifra)
        Label(text = rom_zifra, width = 27, height = 5, font = 90).place(x = 80,y = 20)


    elif a.count ('I') >= 1 or a.count ('i') >= 1 or a.count ('V') >= 1 or a.count ('v') >= 1 or a.count ('X') >= 1 or a.count ('x') >= 1 or a.count ('L') >= 1 or a.count ('l') >= 1 or a.count ('C') >= 1 or a.count ('c') >= 1 or a.count ('D') >= 1 or a.count ('d') >= 1 or a.count ('M') >= 1 or a.count ('m') >= 1 :
        roman = a.upper()                 # позволяет вводить и маленькиими и большими буквами римские цифры.
        print (roman)
        res = 0
        for i, c in enumerate(roman):   # Использую метод enumerate чтобы при переборе достовалось значение переменной.
           if i + 1 < len(roman) and romans_dict[roman[i]] < romans_dict[roman[i + 1]]: # Проверка на исключения по типу IV, IX  где меньшее значение стоит перед большим.
                res -= romans_dict[roman[i]]
           else:
                res += romans_dict[roman[i]]
        
        Label(text = res, width = 27, height = 5, font = 90).place(x = 80,y = 20)


root = Tk()
root.title('переводчик цифр')
root.geometry('400x350')
root.resizable(False, False)
root.config(bg = 'gray')


romans_dict = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
rom_zifra = ''
roman = ''


entry = Entry(root, font = 60)
entry.place(x = 112, y = 120)
Button(text = 'Перевод' , width = 23, height =15  , bg = 'white', command = perivod).place(x = 120, y = 150)
Label(text = 'результат' , width = 27 , height = 5 , font = 90).place(x = 80,y = 20)

root.mainloop()



=======
from tkinter import *

                                                             # Алгоритм автоматически определяет на вводе римские или арабские цифры.
def perivod():
    a = entry.get()
    if a.count('1') >= 1 or a.count('2') >= 1 or a.count('3') >= 1 or a.count('4') >= 1 or a.count('5') >= 1 or a.count('6') >= 1 or a.count('7') >= 1 or a.count('8') >= 1 or a.count('9') >= 1 or a.count('0') >= 1 :
        arabic_zifra = int(entry.get())
        rom_zifra = 'I' * arabic_zifra
        rom_zifra = rom_zifra.replace('IIIII', 'V')
        rom_zifra = rom_zifra.replace('VV', 'X')         # Римская цифра получается путём замены от меньших значений, к большим.
        rom_zifra = rom_zifra.replace('XXXXX', 'L')
        rom_zifra = rom_zifra.replace('LL', 'C')
        rom_zifra = rom_zifra.replace('CCCCC', 'D')
        rom_zifra = rom_zifra.replace('DD', 'M')
        rom_zifra = rom_zifra.replace('DCCCC', 'CM')
        rom_zifra = rom_zifra.replace('CCCC', 'CD')
        rom_zifra = rom_zifra.replace('LXXXX', 'XC')
        rom_zifra = rom_zifra.replace('XXXX', 'XL') 
        rom_zifra = rom_zifra.replace('VIIII', 'IX')
        rom_zifra = rom_zifra.replace('IIII', 'IV') 
        print(rom_zifra)
        Label(text = rom_zifra, width = 27, height = 5, font = 90).place(x = 80,y = 20)


    elif a.count ('I') >= 1 or a.count ('i') >= 1 or a.count ('V') >= 1 or a.count ('v') >= 1 or a.count ('X') >= 1 or a.count ('x') >= 1 or a.count ('L') >= 1 or a.count ('l') >= 1 or a.count ('C') >= 1 or a.count ('c') >= 1 or a.count ('D') >= 1 or a.count ('d') >= 1 or a.count ('M') >= 1 or a.count ('m') >= 1 :
        roman = a.upper()                 # позволяет вводить и маленькиими и большими буквами римские цифры.
        print (roman)
        res = 0
        for i, c in enumerate(roman):   # Использую метод enumerate чтобы при переборе достовалось значение переменной.
           if i + 1 < len(roman) and romans_dict[roman[i]] < romans_dict[roman[i + 1]]: # Проверка на исключения по типу IV, IX  где меньшее значение стоит перед большим.
                res -= romans_dict[roman[i]]
           else:
                res += romans_dict[roman[i]]
        
        Label(text = res, width = 27, height = 5, font = 90).place(x = 80,y = 20)


root = Tk()
root.title('переводчик цифр')
root.geometry('400x350')
root.resizable(False, False)
root.config(bg = 'gray')


romans_dict = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
rom_zifra = ''
roman = ''


entry = Entry(root, font = 60)
entry.place(x = 112, y = 120)
Button(text = 'Перевод' , width = 23, height =15  , bg = 'white', command = perivod).place(x = 120, y = 150)
Label(text = 'результат' , width = 27 , height = 5 , font = 90).place(x = 80,y = 20)

root.mainloop()



>>>>>>> Stashed changes
