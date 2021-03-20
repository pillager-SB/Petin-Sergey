import re
import json

with open('nginx_logs', 'r', encoding='utf-8') as f:
    with open('nginx_logs.json', 'w', encoding='utf-8') as ff:
        for line in f:
            # Так как документ строго структурирован и в задании не требуется проверка данных,
            # то данные просто выхватываются "по месту",
            # исключение составляют только <response_code> - как я понял, это коды записываемые трехзачным числом.
            # и еще <response_size>, считается нормальным, если значение равно нулю или больше.

            prog = re.compile(r'^(?P<remote_addr>.+) - - \[(?P<request_datetime>.+)] "(?P<request_type>.+)'
                              r' (?P<requested_resource>/.+) (.+\" )(?P<response_code>\d{3}) '
                              r'(?P<response_size>\d+)')

            re_date = re.match(prog, line)

            # Использовал именованные группы, благо названия дали "в формате" прямо в задании.

            string = re_date.group('remote_addr', 'request_datetime', 'request_type', 'requested_resource',
                                   'response_code', 'response_size')

            print(string)  # В задании нет указания в каком виде нужно вывести данные, поэтому вывел и через print
            # и в файл json (для красоты)))
            json.dump(string, ff, ensure_ascii=False, indent=4)
