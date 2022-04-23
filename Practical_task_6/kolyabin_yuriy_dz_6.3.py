import sys
from itertools import zip_longest
import json

with open('users.csv', encoding='utf-8') as f1:
    with open('hobby.csv', encoding='utf-8') as f2:
        rows_f1 = f1.read().split('\n')
        rows_f2 = f2.read().split('\n')
        vcb = {key: value if len(rows_f1) > len(rows_f2) else sys.exit(1) for key, value in
               zip_longest(rows_f1, rows_f2[:len(rows_f1)], fillvalue=None)}
with open('vcb.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(vcb, ensure_ascii=False, indent=4))
with open('vcb.json', encoding='utf-8') as f:
    print(f.read(), '\n', type(f.read()))
