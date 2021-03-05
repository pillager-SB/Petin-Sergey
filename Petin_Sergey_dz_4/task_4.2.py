from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(valute):
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    v_pos = content.find(valute.upper())
    if v_pos == -1:
        return None
    c_s_pos = (content.find('<Value>', v_pos) + len('<Value>'))
    c_e_pos = content.find('</Value>', c_s_pos)
    cours = float(content[c_s_pos:c_e_pos].replace(',', '.'))

    return cours


print(currency_rates('EUR'), currency_rates('Usd'))
