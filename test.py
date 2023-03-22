seq=[2,3,4,5,6,7]
p=10
take=filter(lambda x: p-x>5,seq)
print(list(take))