Money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit =[]
for key in per_cent:
    deposit.append(per_cent[key] * Money / 100)
print(deposit)
maximum_amount = max(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(maximum_amount))