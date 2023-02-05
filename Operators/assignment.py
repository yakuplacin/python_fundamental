x, y, z = 512, 234, 204

x, y = y, x

x = x + 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
x //= 5
x **= y

values = 1, 2, 3  # it was tuple
a, b, c = values
print(a, b, c)

values = 1, 2, 3, 4, 5
# here, p will be array that keeps the last 2 element after t and u (1,2)
t, u, *p = values
print(t, u, p)
print(p[1])
