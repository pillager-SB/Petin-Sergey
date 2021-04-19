class Apparats:  # Класс-предок для всех классов оборудования
    def __init__(self, device_type, device_name, interfaces, id_storage, quantity):
        self.device_type = device_type
        self.device_name = device_name
        self.interfaces = interfaces
        self.id_storage = id_storage
        self.quantity = quantity


class Printers(Apparats):
    def __init__(self, device_type, device_name, prn_type, color_type, dpi_prn, sheet_size_prn, interfaces,
                 cartridge, id_storage, quantity):
        Apparats.__init__(self, device_type, device_name, interfaces, id_storage, quantity)
        self.prn_type = prn_type
        self.color_type = color_type
        self.dpi_prn = dpi_prn
        self.sheet_size_prn = sheet_size_prn
        self.cartridge = cartridge

    @staticmethod
    def request_name():
        return 'Тип принтера: ', 'Цветность печати: ', 'Разрешение печати т/д: ', 'Max размер листа (A4,A3 etc): ', \
               f'Интерфейс устройства\nЕсли возможно подключение по нескольким интерфейсам,\n' \
               f'введите их названия через запятую: ', \
               f'Картридж\nЕсли картриджей несколько, введите их названия через запятую: '

    def str_gen(self):
        new_str = (f'{self.device_type};{self.device_name};{self.prn_type};{self.color_type};{self.dpi_prn};'
                   f'{self.sheet_size_prn};{self.interfaces};{self.cartridge};'
                   f'{self.id_storage};{self.quantity}')
        return new_str


class Scanners(Apparats):
    def __init__(self, device_type, device_name, scan_type, dpi_scan, sheet_size_scan, interfaces, id_storage,
                 quantity):
        Apparats.__init__(self, device_type, device_name, interfaces, id_storage, quantity)
        self.scan_type = scan_type
        self.dpi_scan = dpi_scan
        self.sheet_size_scan = sheet_size_scan

    @staticmethod
    def request_name():
        return 'Тип сканнера: ', 'Разрешение сканирования т/д: ', 'Max размер скана (A4,A3 etc): ', \
               f'Интерфейс устройства\nЕсли возможно подключение по нескольким интерфейсам,\n' \
               f'введите их названия через запятую: '

    def str_gen(self):
        new_str = (f'{self.device_type};{self.device_name};{self.scan_type};{self.dpi_scan};'
                   f'{self.sheet_size_scan};{self.interfaces};'
                   f'{self.id_storage};{self.quantity}')
        return new_str


class Copiers(Printers, Scanners):
    def __init__(self, device_type, device_name, prn_type, color_type, dpi_prn, sheet_size_prn, interfaces, cartridge,
                 dpi_scan, sheet_size_scan, id_storage, quantity):
        Printers.__init__(self, device_type, device_name, interfaces, id_storage, prn_type, color_type, dpi_prn,
                          sheet_size_prn, cartridge, quantity)

        Scanners.__init__(self, device_type, device_name, interfaces, id_storage, dpi_scan, sheet_size_scan,
                          quantity, quantity)

    @staticmethod
    def request_name():
        return 'Тип принтера: ', 'Цветность печати: ', 'Разрешение печати т/д: ', 'Max размер листа (A4,A3 etc): ', \
               f'Интерфейс устройства\nЕсли возможно подключение по нескольким интерфейсам,\n' \
               f'введите их названия через запятую: ', 'Картридж\nЕсли картриджей несколько, ' \
                                                       'введите их названия через запятую: ', \
               'Разрешение сканирования т/д: ', 'Max размер скана (A4,A3 etc): '

    def str_gen(self):
        new_str = (f'{self.device_type};{self.device_name};{self. prn_type,};{self.color_type};{self.dpi_prn};'
                   f'{self.sheet_size_prn};'
                   f'{self.interfaces};{self.cartridge};{self.dpi_scan};{self.sheet_size_scan};{self.id_storage};'
                   f'{self.quantity}')
        return new_str


