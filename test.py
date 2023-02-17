a=[1,2,3]
b=[4,6,7]
c=[7,8,9]
d=list(zip(a,b,c))
print(list(map(list,*d[::-1])))