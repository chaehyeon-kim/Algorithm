#1384 

n = 1
group_num = 1

while True:
    n = int(input())
    if(n == 0):break

    arr = [list(map(str, input().split())) for _ in range(n)]
    print('Group', group_num)
    
    num = 0
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == 'N'): 
                s = i + j + 1
                if(s > n):
                    s = s - n
                print(arr[s][0], ' was nasty about ', arr[i][0])
                num += 1
    if(num == 0):
        print('Nobody was nasty')
            
    print()
    group_num += 1
