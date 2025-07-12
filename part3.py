data = [

    ['100','110', '120'],
    ['400','500', '600'],
    ['150','130', '140']

    ]

list = []

for row in data:
    for item in row:
        item = float(item)
        if item > 190:
            list.append(item)

print(list)