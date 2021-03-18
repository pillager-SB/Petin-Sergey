import os
import django


def dir_info():
    root_dir = django.__path__[0]
    django_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(
                str(os.stat(os.path.join(root, file)).st_size))  # разрядность числа получаем из количества
            # знаков размера файла, и возводим 10 в эту степень,, используем как ключ.
            if size in django_files:
                django_files[size][0] += 1  # Наращиваем соответствующий ключ на 1
            else:
                django_files[size] = [1]

    for size, nums in sorted(django_files.items()):
        print(f'{size}: {nums}')


if __name__ == '__main__':
    dir_info()
