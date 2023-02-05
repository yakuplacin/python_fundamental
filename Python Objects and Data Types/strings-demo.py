website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

charLen = len(course)

print(charLen)

result = website[7:10]
print(result)

# result = website[22:25]
webLen = len(website)
result = website[webLen-3:webLen]
print(result)

# result = course[0:15]
result = course[:15]
result = course[-15:]

#tersten yazdırma:
result = course[::-1]
print(result)

y = "12345" * 5  #5 times 12345 it will be like: 1234512345...45
result = y[::5]
print(result)

name, surname, age, job = "Yakup", "LAÇIN", 22, "Student"

result = "Name: {} {}, Age: {}, the job: {}".format(name,surname,age,job)
print(result)

restult = f"Name: {name} {surname}, Age: {age}, the job: {job}"
print(restult)

s = "Hello world!"
s = s.replace("w","W")
print(s)
print(s)