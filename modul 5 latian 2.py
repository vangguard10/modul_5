# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:56:50 2022

@author: fariz
"""

print('''calculating zoo ticket program
==================================''')
x=1
total=0
banyak_data=0
print('press <ENTER> on age to see the result')
while x == 1:
    umur=(input('age:'))
    if umur=='':
        x=-1
        print('====================')
    elif int(umur) <= 2 and int(umur) >= 0:
        uang=int(input('money:'))
        banyak_data+=1
        kembali= uang-0
        x=1
        print('price :free')
        print(f'return: {kembali} dollar')
        print('====================')
    elif (int(umur)>=3) and (int(umur)<=12):
        uang=int(input('money:'))
        kembali= uang-14
        if kembali>0:
            banyak_data+=1
            total+=14
            print(f'return: {kembali} dollar')
            print('====================')
        else:
            print('error')
            print('====================')
        print('price:14 dollar')
        print('====================')
       
        x=1
    elif (int(umur)>12) and int(umur)<65:
        uang=int(input('money:'))
        kembali= uang-23
        if kembali>0:
            banyak_data+=1
            total+=23
            print(f'return: {kembali} dollar')
            print('====================')
        else:
            print('error')
            print('====================')
        print('''price:23 dollar
====================''')
       
        x=1
    elif int(umur)>=65:
        uang=int(input('money:'))
        kembali= uang-18
        if kembali>0:
            banyak_data+=1
            total+=18
            print(f'return: {kembali} dollar')
            print('====================')
        else:
            print('error')
            print('====================')
        print('price:18 dollar')
        print('====================')
       
        x=1
        

print(f'total income: {total} dollar')
print(f'total ticket sold: {banyak_data}')
