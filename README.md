Доделал склад, и он даже работает!)
разделил программу на несколько модулей:
Menu.py - В класс Menu собраны методы для работы с интерфейсом программы, а так же для организовано взаимодействие с другими модулями.
Apparats.py -  объявление базовых классов для оборудования и генерация строк для записи в базу данных.
Storage.py - в классе Storage собраны методы связанные с действиями на складе (проверки, изменения в базе, сортировка и т.д.)
basa.txt - это рабочий файл базы.
baza.txt - копия файла basa.txt.
Для работы программы нужно запустить Menu.py (запускал в PyCarm-е)

У меня есть несколько вопросов:
В Apparats.py я пытался организовать наследование классов:
class Apparats - как базовый класс.
class Printers(Apparats) и class Scanners(Apparats) - как его потомков
class Copiers(Printers, Scanners) - как потомка, соответственно, от Printers и Scanners.
Проблемы возникли с объявлением последнего класса:

class Copiers(Printers, Scanners):
    def __init__(self, device_type, device_name, prn_type, color_type, dpi_prn, sheet_size_prn, interfaces, cartridge,
                 dpi_scan, sheet_size_scan, id_storage, quantity):
        Printers.__init__(self, device_type, device_name, interfaces, id_storage, prn_type, color_type, dpi_prn,
                          sheet_size_prn, cartridge, quantity)

        Scanners.__init__(self, device_type, device_name, interfaces, id_storage, dpi_scan, sheet_size_scan,
                          quantity, quantity) 
                          
1. Почему-то по разному подсвечен синтаксис для Printers.__init__ и Scanners.__init__.
2. Для Scanners.__init__ пришлось дважды ввести аргумент quantity, если оставить один, то появляется сообщение: Parameter 'quantity' unfilled
