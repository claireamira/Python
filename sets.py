set1 = {1, 3, 2, 7, 13, 4}
set2 = {5, 3, 6, 9, False}

print(set1 - set2)

set1.remove(7)
print(set1)

print(len(set2))

set1.add(12)
#NO DUPLICATES IN SETS

set1.update(set2)