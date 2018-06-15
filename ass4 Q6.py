import operator

d = eval(input('Enter Dictionary: '))

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print(sorted_d)
