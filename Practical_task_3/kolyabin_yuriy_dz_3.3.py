def thesaurus(*args):
    employees = dict()
    for name in sorted(list(args)):
        if name[0] not in employees:
            employees[name[0]] = []
        employees[name[0]].append(name)
    return employees


print(thesaurus('Bill', 'Fill', 'Kate', 'Andy', 'Anna', 'Boris', 'Adam', 'Bob'))
