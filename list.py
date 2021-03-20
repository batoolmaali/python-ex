import math

#EX1:
numbers = [1,2,3,4,5,1,4,5] 
summ=sum(numbers)
print(summ)

#EX2:
list1 = [3, 2, 4]
result1 = math.prod(list1)
print(result1)

#EX3:
num=[5,8,1,7,10]
maxVal=max(num)
print(maxVal)

#EX4:
num=[5,8,1,7,10]
minVal=min(num)
print(minVal)

#EX6:
y = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
y.sort(reverse=False)
print(y)

#EX7:
x = [1, 2, 3, 4, 5,"Ayham","Ayham"]
z=list(dict.fromkeys(x))
print(z)

#EX8:
li = []
if not li:
  print("List is empty")

#EX9:
list1 = ["Batool","Tala","Rahaf"]
copy_list = list(list1)
print(list1)
print(copy_list)  

#EX11:
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

#EX12:
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#EX13:
array = [[ ['#' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#EX14:
num = [18,11,24,36,5,9]
num = [x for x in num if x%2!=0]
print(num)

