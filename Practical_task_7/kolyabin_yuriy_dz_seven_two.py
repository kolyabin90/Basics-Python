import os


def create_a_project():
    """Функция создаёт из config.yaml стартер для проекта"""
    with open('config.yaml', encoding='utf-8') as f:
        rows_f = f.read().split('\n')
        for name in rows_f:
            if not name.startswith(' '):
                level_1 = os.path.join('./', name)
                os.makedirs(level_1, exist_ok=True)
            elif name.startswith(' ' * 16):
                level_5 = os.path.join(level_4, name.replace(' ', ''))
                if len(name.split('.')) == 2:
                    with open(level_5, 'a', encoding='utf-8'):
                        pass
                else:
                    os.makedirs(level_5, exist_ok=True)
            elif name.startswith(' ' * 12):
                level_4 = os.path.join(level_3, name.replace(' ', ''))
                os.makedirs(level_4, exist_ok=True)
            elif name.startswith(' ' * 8):
                level_3 = os.path.join(level_2, name.replace(' ', ''))
                if len(name.split('.')) == 2:
                    with open(level_3, 'a', encoding='utf-8'):
                        pass
                else:
                    os.makedirs(level_3, exist_ok=True)
            elif name.startswith(' ' * 4):
                level_2 = os.path.join(level_1, name.replace(' ', ''))
                os.makedirs(level_2, exist_ok=True)


if __name__ == '__main__':
    create_a_project()
