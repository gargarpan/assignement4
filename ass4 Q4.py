"""s = set([1,2,3,4,5,6])


print(s)

s4=set([2,3,5,6,7,8])
print(s1)

s3=s4-s
print(s3)"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

print(set1.union(set2))

print(set1 & set2)

print("itersection is",set1.intersection(set2))

print("difference",set1 - set2)

print(set1.difference(set2))

print(set1 ^ set2)

print(set1.symmetric_difference(set2))
