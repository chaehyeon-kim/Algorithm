#1032

n = int(input())
file = list(input())
file_len = len(file)
for i in range(n - 1):
    name = list(input())
    for j in range(file_len):
        if file[j] != name[j]:
            file[j] = '?'
print(''.join(file))
