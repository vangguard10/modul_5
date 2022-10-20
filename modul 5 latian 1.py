# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:13:12 2022

@author: fariz
"""

print('''A   = 4.00
A-	= 3.75
B+  = 3.50
B   = 3.00
B-	= 2.75
C+  = 2.50
C   = 2.00
C-	= 1.75
D   = 1.50
E   = 1.25
''')
print('press <ENTER> to finish input and calculate')
banyak = 0
jumlah = 0
nilai = 0
while nilai >=0:
    huruf=input('masukan nilai huruf: ')
    if huruf.upper() == 'A':
        banyak+=1
        nilai=4
        jumlah+=4
        print('nilai = 4')
    elif huruf.upper() == 'A-':
        banyak+=1
        nilai=3.75
        jumlah+=3.75
        print('nilai = 3.75')
    elif huruf.upper() == 'B+':
        banyak+=1
        nilai=3.5
        jumlah+=3.5
        print('nilai = 3.5')
    elif huruf.upper() == 'B':
        banyak+=1
        nilai=3
        jumlah+=3
        print('nilai = 3')
    elif huruf.upper() == 'B-':
        banyak+=1
        nilai=2.75
        jumlah+=2.75
        print('nilai = 2.75')
    elif huruf.upper() == 'C+':
        banyak+=1
        nilai=2.5
        jumlah+=2.5
        print('nilai = 2.5')
    elif huruf.upper() == 'C':
        banyak+=1
        nilai=2
        jumlah+=2
        print('nilai = 2')
    elif huruf.upper() == 'C-':
        banyak+=1
        nilai=1.75
        jumlah+=1.75
        print('nilai = 1.75')
    elif huruf.upper() == 'D':
        banyak+=1
        nilai=1.5
        jumlah+=1.5
        print('nilai = 1.5')
    elif huruf.upper() == 'E':
        banyak+=1
        nilai=1.25
        jumlah+=1.25
        print('nilai = 1.25')
    elif huruf.upper() == '':
        nilai=-1
    else:
        print('input tidak benar')
        nilai=0
        
if banyak == 0:
    banyak+=1
else:
    banyak= banyak * 1
    

rata = jumlah/banyak
print('rata rata:',rata)     
