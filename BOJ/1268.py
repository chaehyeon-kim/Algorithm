#1268

st_num = int(input())
arr = [list(map(int,input().split())) for _ in range(st_num)]
cnt = [0] * st_num
for i in range(st_num):
    n = [0] * st_num
    for j in range(5):
        for s in range(st_num):
            if s != i and arr[s][j] == arr[i][j]:
                n[s] = 1
    cnt[i] = sum(n)
print(cnt.index(max(cnt)) + 1)
