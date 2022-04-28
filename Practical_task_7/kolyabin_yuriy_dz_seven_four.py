import os.path

root = os.path.dirname(__file__)
dir_path = os.path.join(root, 'some_data')
keys = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
size_files = {key: 0 for key in keys}
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        sz_f = os.stat(file_path).st_size
        for key in keys:
            if key // 10 < sz_f < key or sz_f == 0:
                size_files[key] += 1
                break
result = {x: y for x, y in size_files.items() if y != 0}
print(result)
