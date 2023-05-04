k, n = map(int, input().split())
c = list(map(int, input().split()))

if len(c) == 1:
    max_attractiveness = c[0] * n
    print(max_attractiveness)
elif n == 1:
    max_attractiveness = max(c)
    print(max_attractiveness)
else:
    max_attractiveness = []
    count = n // k 
    for i in range(count):
        max_attractiveness.extend(c)
    total = 0
    for num in max_attractiveness:
        total += num 
    
    
print (total)