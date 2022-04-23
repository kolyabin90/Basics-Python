from sys import argv
import sys

with open('bakery.csv', encoding='utf-8') as f:
    sales = f.read().split('\n')
    if len(argv) == 1:
        for sale in sales:
            print(sale)
    elif len(argv) == 2:
        for sale in sales[int(argv[1]) - 1:]:
            print(sale)
    elif len(argv) == 3:
        for sale in sales[int(argv[1]) - 1:int(argv[2])]:
            print(sale)
