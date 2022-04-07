#6026
a = input()
b = input()
print(float(a) + float(b))

#6027
x = input()
y = int(x)
print('%x'% y)

#6028
x = input()
y = int(x)
print('%X'% y)

#6029
x = input()
y = int(x, 16)
print('%o'% y)

#6030
x = ord(input())
print(x)

#6031
x = int(input())
print(chr(x))

#6032
x = int(input())
print(-x)

#6033
x = ord(input())
print(chr(x+1))

#6034
x, y = input().split()
print(int(x) - int(y))

#6035
x, y = input().split()
print(float(x) * float(y))

#6036
x, y = input().split()
print(x * int(y))

#6037
x = input()
y = input()
print(y * int(x))

#6038
x, y = input().split()
print(int(x) ** int(y))

#6039
x, y = input().split()
print(float(x) ** float(y))

#6040
x, y = input().split()
print(int(x) // int(y))

#6041
x, y = input().split()
print(int(x) % int(y))

#6042
x = float(input())
print(format(x, ".2f"))

#6043
x, y= input().split()
print(format(float(x) / float(y), ".3f"))

#6044
x, y = input().split()
print(int(x) + int(y))
print(int(x) - int(y))
print(int(x) * int(y))
print(int(x) // int(y))
print(int(x) % int(y))
print(format(int(x) / int(y), ".2f"))

#6045
x, y, z = input().split()
print(int(x)+int(y)+int(z), format((int(x)+int(y)+int(z))/3, ".2f"))

#6046
x = int(input())
print(x * 2)

#6047
x, y = input().split()
print(int(x) * (2 ** int(y)))

#6048
x, y = input().split()
print(int(x) < int(y))

#6049
x, y = input().split()
print(int(x) == int(y))

#6050
x, y = input().split()
print(int(x) <= int(y))
