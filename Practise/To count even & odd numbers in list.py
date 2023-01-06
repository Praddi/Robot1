lst = [1,32,43,45,12,1,3,5]
odd_count,even_count = 0,0
for num in lst:
    if num % 2==0:
        even_count+=1
    else:
        odd_count+=1
print('Even numbers in the list is',even_count)
print('odd numbers in the list is',odd_count)