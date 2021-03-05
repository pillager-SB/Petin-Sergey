from requests import get, utils
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(valute):
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    _ = content.find('Date="') + len('Date="')
    data_num = content[_:_ + 10].replace('.', '')
    date_form = date(int(data_num[-4:]), int(data_num[2:4]), int(data_num[:2]))


    v_pos = content.find(valute.upper())

    if v_pos == -1:
        print(None, date_form)
        return None, date_form

    c_s_pos = (content.find('<Value>', v_pos) + len('<Value>'))
    c_e_pos = content.find('</Value>', c_s_pos)
    cours = float(content[c_s_pos:c_e_pos].replace(',', '.'))

    print(cours, date_form)
    return cours, date_form
