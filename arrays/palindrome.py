# Given an integer x, return true if x is a palindrome, and false otherwise.
# x = 121
# x = 3202023
x=10
# check whether the number is divisible by two
x=str(x)
x = list(x)


# if it is divisible,split into
if len(x) %2 == 0:
    mid_index = len(x)//2
    mid_number = x[mid_index]
    first_half_palindrome=x[0:mid_index]
    second_half_palindrome= x[mid_index:]
# reverse the first set of numbers and compare with the second set
    first_half_palindrome.reverse()
    if first_half_palindrome == second_half_palindrome:
        print(True)
    else:
        print(False)
# if it is not divisible, remove the number in the middle,reverse the first set of numbers and compare with the second set
else:
    mid_index = len(x) // 2
    mid_number = x[mid_index]
    first_half_palindrome = x[0:mid_index]
    second_half_palindrome = x[mid_index+1:]
    first_half_palindrome.reverse()
    if first_half_palindrome == second_half_palindrome:
        print(True)
    else:
        print(False)