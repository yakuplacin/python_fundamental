nm = int(input("Number"))

primary = True

if nm == 1:
    primary = False

for i in range(2, nm):
    if (nm % i == 0):
        primary = False
        break
print(primary)
