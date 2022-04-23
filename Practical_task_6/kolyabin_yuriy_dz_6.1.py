def txt_parsing(txt, start):
    res = txt.split(start)[1:]
    res = res[0].split(' ')[:2]
    return res


file_name = 'nginx_logs.txt'
with open(file_name, encoding='utf-8') as f:
    result = [(remote_address := row.split()[0],
               request_type := txt_parsing(row, '"')[0],
               requested_resource := txt_parsing(row, '"')[1]) for row in f]
print(result)
