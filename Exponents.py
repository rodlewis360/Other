list1 = list(range(1, 101))
list2 = []
for a in list1:
    b = a + 1
    if a ** b == b ** a:
        list2.append(1)
    else:
        list2.append(0)
b = 0
for a in list2:
    b += a
    c += 1
average = b / c
averagepercent = average * 100
print("This algorithm is correct",averagepercent,"% of the time!")
