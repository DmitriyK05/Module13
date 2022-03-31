count = int(input('Кол-во билетов: '))
result = 0
for i in range(count):
    age = int(input('Возраст: '))
    if 18 <= age < 25:
        result += 990
    elif 25 <= age:
        result += 1390
if count > 3:
    result = result - result // 10
print(result)
