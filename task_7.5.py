import os
import django
import json


def dir_info():
    root_dir = django.__path__[0]
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            f_ext = file.rsplit('.', maxsplit=1)[-1]  # находим расширение
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))  # разрядность числа получаем из количества
            # знаков размера файла, и возводим 10 в эту степень, используем как ключ.
            if size in django_files:
                django_files[size][0] += 1
                if f_ext not in django_files[size][1]:
                    django_files[size][1].append(f_ext)
            else:
                django_files[size] = [1, [f_ext]]

    result = {}
    for size, count_and_f_ext in sorted(django_files.items()):
        count_and_f_ext[1] = sorted(count_and_f_ext[1])
        result[size] = count_and_f_ext
        print(f'{size}: {tuple(count_and_f_ext)}')
    folder_name = os.path.dirname(__file__).split('\\')[-1] + '_summary.json'
    with open(folder_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    dir_info()
