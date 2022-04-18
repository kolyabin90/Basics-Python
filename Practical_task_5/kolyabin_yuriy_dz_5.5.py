src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
recurring = set()
for i in src:
    if i in recurring:
        continue
    if i in unique:
        recurring.add(i)
        unique.discard(i)
        continue
    unique.add(i)
print([i for i in src if i in unique])
