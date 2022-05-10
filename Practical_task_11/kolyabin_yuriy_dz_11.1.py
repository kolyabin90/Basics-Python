# import time


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        date_lst = date.split('-')
        for i, el in enumerate(date_lst):
            if int(el):
                date_lst[i] = int(el)
            else:
                raise ValueError(f'Ошибка в дате!')
        return date_lst

    @staticmethod
    def is_valid_or_not(date):

        # try:
        #     time.strptime(date, '%d-%m-%Y')
        # except ValueError:
        #     return f'{date} такой даты не может быть!'
        # return f'{date} коррeктна.'

        date_ = Date.convert(date)
        corr = f'{date} is correct.'
        not_corr = f'{date} is not correct.'
        day, month, year = date_[0], date_[1], date_[2]
        d_m = {'30': [4, 6, 9, 11], '31': [1, 3, 5, 7, 8, 10, 12]}
        if month == 2 and 1 <= day <= 29 and year % 4 == 0:
            return corr
        elif 1 <= day <= 28 and 1 <= month <= 12:
            return corr
        elif (day == 30 or 31) and month in d_m['31']:
            return corr
        elif day == 30 and month in d_m['30']:
            return corr
        else:
            return not_corr


date_1 = '30-12-2020'
print(Date.is_valid_or_not(date_1))
date_2 = '30-02-2005'
print(Date.is_valid_or_not(date_2))
date_3 = '31-09-2022'
print(Date.is_valid_or_not(date_3))
date_4 = '29-02-2024'
print(Date.is_valid_or_not(date_4))
