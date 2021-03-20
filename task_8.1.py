import re


class CustomError(Exception):
    pass


class IllegalSymbolError(CustomError):  # В имени аккаунта содержатся запрещеные символы.[&=+<>,_\s-]+|[.]{2,}]
    pass


class MissingSymbolError(CustomError):  # В имени аккаунта отсутствует символ @.
    pass


class MissingPointError(CustomError):  # В имени аккаунта нет ни одной точки после @.
    pass


def email_parse(email_address):
    txt = email_address
    try:
        re_date = re.search(r'^[.]+|[.]+@|[&=+<>,_\s-]+|[.]{2,}', txt)
        if re_date:
            raise IllegalSymbolError
        re_date = not re.search('@', txt)
        if re_date:
            raise MissingSymbolError
        re_date = not re.search('@\w+[.]+\w+', txt)
        if re_date:
            raise MissingPointError
        re_date = re.split('@', txt, maxsplit=1)
        prn = {'username': re_date[0], 'domain': re_date[1]}
        return prn

    except IllegalSymbolError:
        return f'В имени аккаунта {txt} содержатся недопустимые символы.'
    except MissingSymbolError:
        return f'В имени аккаунта {txt} отсутствует символ @.'
    except MissingPointError:
        return f'В имени аккаунта  {txt} после @ нет ни одной точки.'


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someonegeekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
    print(email_parse('.someone@geekbrains.ru'))
