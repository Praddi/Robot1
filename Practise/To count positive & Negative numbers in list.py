list1 = [1,2,-3,4,-5,-6,7,8,9,-10,-11,-12,-13,14,15,16]
only_pos = [num for num in list1 if num >=1]
pos_count = len(only_pos)

print(pos_count)
print(len(list1) - pos_count)