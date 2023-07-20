nums = [0, 1, 0, 1, 2, 4, 2, 1, 3, 3]

# check length of array is zero, if not continue
if len(nums) == 0:
    print(nums)
else:
    # check length of array is one, if not continue
    # create a new array
    new_array = []
    n = 0
    #  add value of nums array in new array
    new_array.append(nums[n])
    # check  if the value in new array is in nums array
    for value in nums:
        if value in new_array:
            print(new_array)
            n += 1
        else:
            new_array.append(value)
            print(new_array)
# if the value is in nums array, do not append value in new array
# move to the next value in nums array
#  repeat this till the end of the array
