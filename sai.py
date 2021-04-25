s="+-*/%"
import itertools
lis = list(itertools.combinations_with_replacement (s,2))
lis1= list(itertools.combinations_with_replacement (s,3))
lis2= list(itertools.combinations_with_replacement (s,4))
res =[]
for i in lis:
    res.append("".join(list(i)))
for i in lis1:
    res.append("".join(list(i)))
for i in lis2:
    res.append("".join(list(i)))

oc_list = res