list1 = [10, 21, 4, 45, 66, 93]
for i in list1:
    if i % 2 !=0:
        print(i,end=" ")

list1 = [10, 21, 4, 45, 66, 93]
a=[i for i in list1 if i % 2 !=0]
print(a)

list1 = [10, 21, 4, 45, 66, 93]
a=[i for i in list1 if i % 2 ==1]
print(a)


