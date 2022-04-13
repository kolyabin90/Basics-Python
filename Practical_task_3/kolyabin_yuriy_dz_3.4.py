def thesaurus_adv(*args):
    surname = dict()
    peoples = sorted(args, key=lambda x: x.split()[-1])
    for name in peoples:
        key_surname = name.split()[-1][0]
        key_name = name[0]
        if key_surname not in surname:
            surname[key_surname] = dict()
        if key_name not in surname[key_surname]:
            surname[key_surname][key_name] = []
        surname[key_surname][key_name].append(name)
    return surname


print(thesaurus_adv('Роман Попов', 'Федор Бондарчук', 'Александра Бортич', 'Андрей Меньшиков',
                    'Aлла Пугачева', 'Борис Ельцин', 'Виктор Янукович', 'Александра Яковлева'))
