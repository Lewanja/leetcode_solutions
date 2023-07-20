nums=[0,1,0,1,2,4,2,1,3,3]

# dictionary that stores elements in nums
nums_dict = {}
# loop through list, if number is not in dictionary add it to the dictionary
index=0
while index < len(nums):
    element = nums[index]
    if element not in nums_dict.keys():
        nums_dict[element]=element
        print(nums)
        print(nums_dict)
        index += 1
    # if it is in the dictionary remove in array
    else:
        nums.remove(element)
        print(nums)
