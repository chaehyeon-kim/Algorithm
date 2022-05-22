#1652

n=int(input())
arr=[]
for i in range(n):
    str =input()
    arr.append(list(str))
    
col = 0
row = 0
cnt = [[0] * n]*n

print(cnt)
print(arr)
for i in range(n):
    for j in range(n):
        if(arr[i][j] == 'X'):
            if(cnt[i][j] == 1):
                break
            cnt[i][j] = 1
        elif(arr[i][j] == '.'):
            cnt[i][j] = 0
        if(cnt[i][j] == 1):
            row += 1
    if(cnt[i][j] == 1):
        col += 1
        
print(cnt)
print("row",row)
print("col",col)
