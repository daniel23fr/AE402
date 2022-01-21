# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:38:12 2021

@author: alice
"""

 
num=0
price=0
sell=0
sells=[]

print('########################')
print('###Python蘋果店進出貨系統###')
print('########################')

while True:
    
    print('功能=>')
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存顯示')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')
    
    if(sel == '1'):
        print('進入設定功能')
        apple = int(input('請問有幾顆蘋果?'))
        money = int(input('請問一顆蘋果多少錢?'))
        num = apple
        price = money
        print('現在共有' + str(num) + '顆蘋果')
        print('一顆蘋果' + str(price) + '塊錢')
    elif(sel == '2'):
        print('進入進貨功能')
        apple = int(input('請問買了幾顆蘋果?'))
        num = num + apple
        print('現在共有' + str(num) + '顆蘋果')
    elif(sel == '3'):
        print('進入出貨功能')
        apple = int(input('請問賣了幾顆蘋果?'))
        print('應該要付' + str(apple * price) + '塊錢')
        sell = sell + apple * price
        sells.append(apple)
    elif(sel == '4'):
        print('進入營業額統計功能')
        for i in range(len(sells)):
            print('賣了' + str(sells[i]) + '顆蘋果 共' + str(sells[i]*price) + '塊錢')
        print('總共賺了' + str(sell) + '塊錢')
    elif(sel == '5'):
        print('進入庫存顯示功能')
        print('現在共有' + str(num) + '顆蘋果')
    elif(sel == '6'):
        print('離開系統')
        break
