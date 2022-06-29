dct={0:{'pos':0,'neg':0},1:{'pos':1,'neg':0},2:{'pos':2,'neg':0},3:{'pos':0,'neg':3},
     4:{'pos':1,'neg':4},5:{'pos':5,'neg':2},6:{'pos':3,'neg':6},7:{'pos':7,'neg':4}}

print(max([k[0] for k in [list(i.values()) for i in dct.values()]]))