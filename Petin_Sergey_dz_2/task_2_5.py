# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
price_list = [520, 0.8, 138.8, 135.26, 1.33, 300.82, 185.7, 502.23, 420.97, 107.38, 202.97,
              78.84, 361.96, 430.76, 380.35, 332.27, 108.72, 432.52, 108.71, 42.02]
print(f'{id(price_list)} (id исходного списка) ', end='/// Прайслист 1: ')
for n in price_list:
    if n == price_list[-1]:
        end_print = '\n'
    else:
        end_print = ', '
    print(f'{int(n):02d} руб {(int(n*100) % 100):02d} коп', end=end_print)

price_list.sort()
print(f'{id(price_list)} (id отсортированного списка)', end='/// Прайслист 2: ')
for n in price_list:
    if n == price_list[-1]:
        end_print = '\n'
    else:
        end_print = ', '
    print(f'{int(n):02d} руб {(int(n*100) % 100):02d} коп', end=end_print)

price_list2 = sorted(price_list, reverse=True)
print(f'{id(price_list2)} (id вновь отсортированного списка)', end='/// Прайслист 3: ')
for n in price_list2:
    if n == price_list2[-1]:
        end_print = '\n'
    else:
        end_print = ', '
    print(f'{int(n):02d} руб {(int(n*100) % 100):02d} коп', end=end_print)

print('Вывод цен пяти самых дорогих товаров', end='/// Прайслист 4: ')

for n in price_list2[:5]:
    if n == price_list2[4]:
        end_print = '\n'
    else:
        end_print = ', '
    print(f'{int(n):02d} руб {(int(n*100) % 100):02d} коп', end=end_print)

print('Вывод цен пяти самых дорогих товаров сортировка по возрастанию', end='/// Прайслист 5: ')

for n in price_list2[4::-1]:
    if n == price_list2[0]:
        end_print = '\n'
    else:
        end_print = ', '
    print(f'{int(n):02d} руб {(int(n*100) % 100):02d} коп', end=end_print)
