import heapq
s=[
    [1,True],
    [2,False],
    [3,True],
    [4,False]
]

heapq.heapify(s)

smallest=heapq.nsmallest(n=1,iterable=s,key=lambda l: l[1])

print(smallest)

# print(sorted(s,key=lambda l: [l[1],-l[0]]))