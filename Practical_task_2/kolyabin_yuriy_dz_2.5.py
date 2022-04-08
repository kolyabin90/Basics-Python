prices = [57.8, 46.51, 97, 23.76, 78.09, 109, 45.12, 93.71, 12.09, 40]
for i in prices:
    print(f'{int(i)} руб {(round((i - int(i)) * 100)):02d} коп', end=', ')
print('')
prices_sort = prices[:]
prices_sort.sort()
for i in prices_sort:
    print(f'{int(i)} руб {(round((i - int(i)) * 100)):02d} коп', end=', ')
print('')
print(prices)
prices_rvs = prices.copy()
prices_rvs = sorted(prices_rvs, reverse=True)
for i in prices_rvs[:5]:
    print(f'{int(i)} руб {(round((i - int(i)) * 100)):02d} коп', end=', ')
