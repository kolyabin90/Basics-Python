from requests import get
import datetime


def pull_out(site, start, stop):
    result = []
    for _ in site.split(start)[1:]:
        result.append((_.split(stop)[0]))
    return result


def currency_rates(abbrev):
    content = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    date = pull_out(content, 'Date="', '"')
    date = date[0]
    datetime.datetime.strptime(date, "%d.%m.%Y")
    abbrev = abbrev.lower().upper()
    abbreviation = pull_out(content, '<CharCode>', '</CharCode>')
    result = None
    if abbrev not in abbreviation:
        return result
    else:
        amount_of_money = pull_out(content, '<Nominal>', '</Nominal>')
        translation_ru = pull_out(content, '<Name>', '</Name>')
        value = pull_out(content, '<Value>', '</Value>')
        index = abbreviation.index(abbrev)
        result = float(value[index].replace(',', '.'))
        return f'{amount_of_money[index]} {abbreviation[index]}({translation_ru[index]}) = {result} RUB.' \
               f' Курс от {date} года.'


if __name__ == '__main__':
    print(currency_rates('Usd'))
    print(currency_rates('eu'))
    print(currency_rates('EUR'))
