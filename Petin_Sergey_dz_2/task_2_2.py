start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
fin_list = []
for n in start_list:
    if not n[-1].isdigit():
        fin_list.append(n)
    else:
        _ = ''
        if len(n) == 1:
            _ = '"' + '0' + n + '"'
            fin_list.append(_)
            continue
        elif n[0].isdigit():
            _ = '"' + n + '"'
            fin_list.append(_)
            continue
        if ord(n[0]) == 43 or 45:
            _ = '"' + n[0] + '0' + n[-1] + '"'
            fin_list.append(_)

print(' '.join(fin_list))
