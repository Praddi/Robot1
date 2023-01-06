l = [1,2,2,3,4,4,4,5,1,2,3,4,5]
ele = 1
x = [i for i in l if i==ele]
print('the element',ele,'occurs',len(x),'times')

import pandas
l = [1,2,2,3,4,4,4,5,1,2,3,4,5]
count= pandas.Series(l).value_counts()
print('Element count')
print(count)