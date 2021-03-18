import os
import shutil

my_proj = 'my_project'
templates_dir = os.path.join(my_proj, 'templates')


def store():
    for main_dir in os.listdir(my_proj):
        for d in os.scandir(os.path.join(my_proj, main_dir)):  # получаем объект DirEntry()
            if d.name == 'templates' and d.is_dir():  # Если есть папка с именем templates
                s_dir = os.path.join(templates_dir, main_dir)  # формируем путь для последующего сохранения:
                # папка хранения templates + имя папки, где была найдена папка templates
                if not os.path.exists(s_dir):  # Проверка отсутствия папки с таким именем и создание ее.
                    os.makedirs(s_dir)
                else:
                    exit(f'Директория уже существует в папке {my_proj}')
                for root, _, file in os.walk(d):
                    for f in os.scandir(root):
                        if f.is_file():
                            shutil.copyfile(f.path, os.path.join(s_dir, f.name))


if __name__ == '__main__':
    store()
