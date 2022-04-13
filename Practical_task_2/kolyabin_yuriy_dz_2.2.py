txt = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_txt = []
for word in txt:
    if word.isdigit():
        new_txt.extend(['"', f'{int(word):02d}', '"'])
    elif word[0].startswith('+') or word[0].startswith('-'):
        new_txt.extend(['"', f'{word[0]}{int(word):02d}', '"'])
    else:
        new_txt.append(word)
print(new_txt)
result = ''
j = 0
for i in new_txt:
    if i == '"':
        j += 1
        if j % 2 != 0:
            result += i
        else:
            result += i + ' '
    elif i[-1].isdigit():
        result += i
    else:
        result += i + ' '
print(result)

# 2 вариант решения через .join

txt = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_txt = []
for word in txt:
    if word.isdigit():
        new_txt.extend(['"', f'{int(word):02d}', '"'])
    elif word[0].startswith('+') or word[0].startswith('-'):
        new_txt.extend(['"', f'{word[0]}{int(word):02d}', '"'])
    else:
        new_txt.append(word)
print(new_txt)
result = []
j = 0
for i in new_txt:
    if i == '"':
        j += 1
        if j % 2 != 0:
            result.append(i)
        else:
            result.append(i)
            result.append(' ')
    elif i[-1].isdigit():
        result.append(i)
    else:
        result.append(i)
        result.append(' ')
print(''.join(result))
