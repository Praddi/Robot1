#By index method
lst = [10, 20, 4, 45, 99]
lst.sort(reverse=False)
print('Second largest number in list is',lst[-2])

#By removing the largest number in the list
lst = [10, 20, 4, 45, 99]
new_list = lst
new_list.remove(max(new_list))
print(max(new_list))

