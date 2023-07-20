# Given an integer numRows, return the first numRows of Pascal's triangle.
# [1] n=0
# [1,1] n = 1
# [1,2,1]n=2
# [1,3,3,1]n=3
# [1,4,6,4,1]n=4
# [1,5,10,10,5,1]=5
# [1,6,15,20,15,6,1]=6

# take num_rows
# define a list [pascal_integers] that will contain list of pascal integers
# define another list[constants] that will contain added constants
# initialize integer that will be used to add numbers in the list iterated
# start from zero increasing to the number required in numrows
#

num_array= 4
pascal_triangle_array=[]
item=[]
second_item = [1,3,3,1]
index = 0

for value in range(num_array):
    if value == 0:
        item.append(1)
    if value == num_array-1:
        item.append(1)
    else:
        center_value = second_item[index]+second_item[index+1]
        index +=1
        item.append(center_value)
pascal_triangle_array.append(item)
print(item)
print(pascal_triangle_array)

