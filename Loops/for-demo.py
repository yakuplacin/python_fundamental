numbers = [1, 2, 3, 4, 5]
toplam = 0
for value in numbers:
    print(value)
    toplam += value

print(toplam)   
d = {"k1": 1, "k2": 2, "k3": 3}

for key, value in d.items():
    print(key, value)

for i in numbers:
    if (i % 2 == 1):
        print(i**2)

cities = ["Kocaeli", "Istanbul", "Rize", "Kayseri", "Muş"]

for city in cities:
    if (len(city) <= 5):
        print(city)

products = [
    {"name": "samsung6", "price":"3000"},
    {"name": "samsung7", "price":"4000"},
    {"name": "samsung8", "price":"5000"},
    {"name": "samsung9", "price":"6000"},
    {"name": "samsung10", "price":"7000"},   
]

toplam = 0
for product in products:
    toplam += int(product["price"])
print(toplam)

for product in products:
    if int(product["price"]) <= 5000:
        print(product["name"])