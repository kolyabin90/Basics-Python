from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Кирилл', 'Олег', 'Ольга']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
result = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses[:len(tutors)], fillvalue=None))
print(type(result))
for res in result:
    print(res)
