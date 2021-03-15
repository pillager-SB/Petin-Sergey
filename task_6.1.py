with open('nginx_logs', 'r', encoding='utf-8') as f:
    content = [(line.split()[0], line.split()[5][1:], line.split()[6]) for line in f]
    with open('nginx_logs.txt', 'a', encoding='utf-8') as ff:
        ff.write('[\n')
        for i in content:
            ff.write(f'{i},\n')
        poz = ff.tell()
        ff.write(']\n')
