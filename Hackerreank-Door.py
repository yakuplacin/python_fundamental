# c = bin(5)
# print(c)
# print(len(c))

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
# N = int(input())
# M = int(input())

T = T.split(" ")
N = int(T[0])
M = int(T[1])

# N = int(N)
# M = int(M)

i = 0
while i < N//2:
    result = (".|."*(2*i + 1)).center(M,"-")
    print(result)
    i = i + 1

print("WELCOME".center(M,"-"))

i = N//2 - 1
while i >= 0:
    result = (".|."*(2*i + 1)).center(M,"-")
    print(result)
    i = i - 1