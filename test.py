from collections import OrderedDict

dct=OrderedDict()

dct['a']=2
dct['b']=3

v=next(iter(dct))

print(dct.pop(v))
print(dct)