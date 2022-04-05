ticket = int(input("Введите количество билетов, которое вы хотите приобрести: "))
price = 0.0
for i in range(ticket):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        price = 0 + price
    elif 18 <= age < 25:
        price = 990 + price
    else:
        price = 1390 + price
    if 3 < ticket:
        price = 0.9 * price
print("Сумма к оплате равна - " + str(round(price)) + " " "рублей")
