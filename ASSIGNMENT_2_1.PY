# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Lst =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List of Tuple before sorting : " + str(Lst)) 
listLen = len(Lst); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(Lst[j][-1] > Lst[j + 1][-1]):
            # print(Lst)
            swap = Lst[j]
            Lst[j] = Lst[j + 1]
            Lst[j + 1] = swap
print("List of Tuple after sorting : " + str(Lst))