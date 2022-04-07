#6051
x, y = input().split()
print(int(x) != int(y))

#6052
x = int(input())
print(bool(x))

#6053
x = int(input())
print(not(bool(x)))

#6054
x, y = input().split()
print(bool(int(x)) and bool(int(y)))

#6055
x, y = input().split()
print(bool(int(x)) or bool(int(y)))

#6056
x, y = input().split()
x = bool(int(x))
y = bool(int(y))
print((x and (not y)) or ((not x) and y))

#6057
x, y = input().split()
x = bool(int(x))
y = bool(int(y))
print((x and y) or ((not x) and (not y)))

#6058
x, y = input().split()
x = bool(int(x))
y = bool(int(y))
print((not x) and (not y))

#6059
x = int(input())
print(~x)

#6060
x, y = input().split()
print(int(x) & int(y))

#6061
x, y = input().split()
print(int(x) | int(y))

#6062
x, y = input().split()
print(int(x) ^ int(y))

#6063
x, y = input().split()
x = int(x)
y = int(y)
max = 0
if (x > y):
	max = x
else:
	max = y
print(max)

#6064
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
min = 0
if (x > y):
	if (y > z):
		min = z
	else:
		min = y
else:
	if (x > z):
		min = z
	else:
		min = x
print(min)

#6065
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
if (x % 2) == 0:
	print(x)
if (y % 2) == 0:
	print(y)
if (z % 2) == 0:
	print(z)

#6066
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
if (x % 2) == 0:
	print("even")
else:
	print("odd")
if (y % 2) == 0:
	print("even")
else:
	print("odd")
if (z % 2) == 0:
	print("even")
else:
	print("odd")

#6067
x = int(input())
if x < 0:
	if (x % 2) == 0:
		print("A")
	else:
		print("B")
else:
	if (x % 2) == 0:
		print("C")
	else:
		print("D")

#6068
x = int(input())
if (x >= 90):
	print("A")
elif (x >= 70):
	print("B")
elif (x >= 40):
	print("C")
else:
	print("D")

#6069
x = input()
if (x == 'A'):
	print('best!!!')
elif (x == 'B'):
	print('good!!')
elif (x == 'C'):
	print('run!')
elif (x == 'D'):
	print('slowly~')
else:
	print('what?')

#6070
x = int(input())
if (x//3 == 1):
	print("spring")
elif (x//3 == 2):
	print("summer")
elif (x // 3 == 3):
	print("fall")
else:
	print("winter")

#6071
x = 1
while x != 0:
	x = int(input())
	if x != 0:
		print(x)

#6072
x = int(input())
while x != 0:
	print(x)
	x = x - 1

#6073
x = int(input())
while x != 0:
	x = x - 1
	print(x)

#6074
x = ord(input())
i = ord('a')
while i <= x :
  print(chr(i), end=' ')
  i = i + 1

#6075
x = int(input())
i = 0
while i <= x:
	print(i)
	i = i + 1
