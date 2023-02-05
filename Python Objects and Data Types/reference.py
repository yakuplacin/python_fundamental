x = 5
y = 25

x = y  # it works after we change the x or y, it will not affect each one after this code!

y = 222
print(x, y)

# BUT!! FOR REFERENCES, IT IS DIFFERENT BECAUSE IT KEEPS ITS ADDRESS

a = ["apple", "banana"]
b = []

b = a
b[0] = "grape"
print(a, b)  # here, these will be the same!!!!! because they share their address as an array. so any changes will affect both

# instead, use the list()
c = ["peach", "cherry"]
d = list(c)  #here, we just like copy the c array to  the d aray, not the address!!!!!!
#with this list() functionality, we can do that!
d[0] = "Kiwi"
print(d, c)
