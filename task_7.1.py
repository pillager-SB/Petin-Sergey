import os

# Представляем структуру папок в виде списка с вложенным списком.
design = ['my_project', ['settings', 'mainapp', 'adminapp', 'authapp']]

l_dir = os.path.abspath('task_7.1.py')  # Определяем директорию, где находится наш скрипт.
f_dir, _ = os.path.split(l_dir)

dir_name = design[0]
if not os.path.exists(dir_name):  # Проверяю наличие корневой папки, если ее нет - создаю структуру.
    for n in design[1]:
        path_d = os.path.join(design[0], n)
        os.makedirs(path_d)
    n = (os.makedirs(os.path.join(design[0], n)) for n in design[1])
else:
    exit(f'Tакая папка в {f_dir} уже существует')  # Если папка есть - выход с сообщением о существовании такой папки.
