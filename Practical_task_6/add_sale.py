from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write(argv[1])
