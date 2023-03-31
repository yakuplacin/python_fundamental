import mod  # This will automatically call and impırt the mod module that I have written

# result = help(mod)
# result = help(mod.func)

result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]
result = mod.func(20)

p = mod.Person()
p.speak()

print(result)
