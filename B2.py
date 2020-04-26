n = int(input())

nums = []
for i in range(n):
    row = list(map(int, input().split()))
    nums.append(row)

p = 0
x, y = 0, 0
path = []
print(nums)

for i in range(n):
    for j in range(n):
        if nums[i][j] != None:
            path.append('R')
        else:
            j = 1

    path.append('D')


print(path)
input()
