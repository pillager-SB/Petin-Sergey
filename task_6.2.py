with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    d = {}
    content = (line.split(',')[0][1:].strip("'") for line in f)
    for i in content:
        if i in d:
            d[i] = d[i] + 1
        else:
            d.update({i: 1})

end_find = sorted(d.items(), key=lambda kv: kv[1])[-1]
print(f'Spammers ID: {end_find[0]}\nTotal Calls: {end_find[1]} ')

# Spammers ID: 216.46.173.126
# Total Calls: 2350
