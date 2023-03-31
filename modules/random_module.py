import random

# result = dir(random)

# print(result)
# print(help(random))

result = random.random()  # 0 - 1
result = random.random() * 100
result = int(random.uniform(10, 20))
result = random.randint(1, 30)

names = ["Yakup", "Gözde", "Senim", "Doruk", "Şeyma", "Emre"]
result = names[random.randint(0, len(names)-1)]
# this allow us to choice randomly an index from our array
result = random.choice(names)
print(result)

word = "I am using Python!"
# we can also use it as a string with choosing random char
print(random.choice(word))

myList = list(range(10))
random.shuffle(myList)
print(myList)

myList2 = range(100)
result = random.sample(myList2, 3)
print(result)

print(random.sample(names, 2))
