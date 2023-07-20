nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# check if the length of array is 0. If zero end by printing None
if len(nums) == 0:
    print(nums)
else:
    # check if the length of the array is 1, if 1 end the iteration else continue
    if len(nums) == 1:
        print(nums)
    else:
        current_index = 0
        while current_index < len(nums) - 1:
            # loop through the length of the list -1
            # if current number == next number remove next substitute with None
            current_value = nums[current_index]
            # start with value in first index call it current i.e index at current = x
            if current_value == nums[current_index + 1]:
                nums.pop(current_index)
                print(nums)
            else:
                current_index += 1
                print(nums)
# 0, 1, 2 ,3,4,5
# the next number after current is the next integer to compare with, index at next = x + 1
#  compare next and current
# if the values are the same remove next
# assign  current to next
#  if values are not the same retain the next value
