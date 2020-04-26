from heapq import heappush, heappop
from sys import stdin, exit

template = list(next(stdin).strip())
print(template)
n, cost, balance = len(template), 0, 0

min_heap = []

for i in range(n):
    print('balance', balance)
    if template[i] == '(':
        balance += 1
    elif template[i] == ')':
        balance -= 1

    else:
        cost_left, cost_right = map(int, next(stdin).split())
        template[i] = ')'
        cost += cost_right
        balance -= 1
        heappush(min_heap, (cost_left - cost_right, i))
    if balance < 0:
        if not min_heap:
            print(-1)
            exit(0)
        change_cost, index = heappop(min_heap)
        template[index] = '('
        cost += change_cost
        balance += 2

if balance == 0:
    print(cost)
    print(''.join(template))
else:
    print(-1)
