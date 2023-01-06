list1 = [1,2,-3,4,-5,-6,7,8,9,-10,-11,-12,-13,14,15,16]
pos_num = [i for i in range (13) if i % 2==0]
print(pos_num)

#To print negative numbers in list

list1 = [1,2,-3,4,-5,-6,7,8,9,-10,-11,-12,-13,14,15,16]
neg_num = [i for i in range (list1) if i < 0]
print(neg_num)