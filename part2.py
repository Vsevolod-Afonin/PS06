data = [
    ['100','200', '300'],
    ['400','500', '600']

    ]

numbers = []

for row in data:
    for text in row:
        number = float(text)
        numbers.append(number)

print(numbers)