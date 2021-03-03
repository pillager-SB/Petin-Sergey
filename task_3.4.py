def thesaurus_adv(*names):
    result = {}
    for n in sorted(names):
        first_name, last_name = n.split()
        fn = first_name[0]
        ln = last_name[0]
        if ln not in result:
            result[ln] = {}

            if fn not in result[ln]:
                result[ln].update({fn: [n]})

        else:
            if fn not in result[ln]:
                result[ln].update({fn: [n]})
            else:
                result[ln][fn].append(n)

    return sorted(result.items())

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Махмуд Ибрагимов", "Анна Савельева"))