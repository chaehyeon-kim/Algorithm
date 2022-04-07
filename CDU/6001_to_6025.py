#6001
print("Hello")

#6002
print("Hello","World")

#6003
print("Hello")
print("World")

#6004
print("'Hello'")

#6005
print('"Hello World"')

#6006
print(print("\"!@#$%^&*()\'"))

#6007
print('\"C:\Download\\\'hello\'.py\"')

#6008
print("print(\"Hello\\nWorld\")")

#6009
x = input()
print(x)

#6010
x = int(input())
print(x)

#6011
x = float(input())
print(x)

#6012 
a = int(input())
b = int(input())
print(a)
print(b)

#6013 
a = input()
b = input()
print(b)
print(a)

#6014
x = float(input())
for i in range(3):
    print(x)

#6015 
a, b = input().split()
print(a)
print(b)

#6016
a,b = input().split()
print(b, a)

#6017 
x = input()
print(x, x, x)

#6018
hour, min = input().split(':')
print(hour, min, sep=':')

#6019 
y, m, d = input().split('.')
print(d, m, y, sep="-")

#6020 
x, y = input().split("-")
print(x, y, sep="")

#6021
x = input()
for i in range(len(x)):
    print(x[i])

#6022
x = input()
print(x[0:2], x[2:4], x[4:6])

#6023
h, m, s=input().split(":")
print(m)

#6024
w1, w2 = input().split()
print(w1 + w2)

#6025 
a, b = input().split()
print(int(a) + int(b))
