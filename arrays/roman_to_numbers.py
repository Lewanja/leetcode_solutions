# Runtime 51 ms Beats 73.98%
# Memory 14 MB Beats 26.96%

"""
MCMXCIV
M 1000      CMXCIV


have a dict to map letters to their values
have a var sum initially zero
Convert string to list
loop fom left to right while the length of list is not zero. 
    if the length of the list is two or more
        take two elements. get their values from dict above
        if first is greater than second, then pop first only and add it to sum
        if second is greater than first, subtract first from second and pop both from list and add subtotal to sum
        if they are equal add subtotal to sum and pop both from list
    else we only have one element so just add it to total  
"""
import unittest

class Solution:

    def romanToInt(self, s: str) -> int:
        symbol_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_number_list = list(s)
        roman_integer = 0
        print(s)
        while len(roman_number_list) > 0:
            if len(roman_number_list) > 1:

                first_roman_symbol_in_list = roman_number_list[0]
                first_roman_value_in_list = symbol_dict[first_roman_symbol_in_list]
                second_roman_symbol_in_list = roman_number_list[1]

                second_roman_value_in_list = symbol_dict[second_roman_symbol_in_list]
                if first_roman_value_in_list > second_roman_value_in_list:
                    roman_number_list.pop(0)
                    roman_integer += first_roman_value_in_list

                elif first_roman_value_in_list < second_roman_value_in_list:
                    roman_integer += second_roman_value_in_list - first_roman_value_in_list
                    print(roman_number_list)
                    roman_number_list.pop(0)
                    roman_number_list.pop(0)
                else:
                    roman_integer += first_roman_value_in_list * 2
                    roman_number_list.pop(0)
                    roman_number_list.pop(0)

            else:
                roman_integer += symbol_dict[roman_number_list[0]]
                roman_number_list.pop(0)

        return roman_integer

# solution_class_instance = Solution()
# roman_number= solution_class_instance.romanToInt("III")
# print(roman_number)

class SolutionTest(unittest.TestCase):
    def test_roman_numbers_1994(self):
        roman_symbol = "MCMXCIV"
        expected_roman_symbol = 1994
        roman_solution = Solution().romanToInt(roman_symbol)
        self.assertEqual(roman_solution, expected_roman_symbol)
    def test_roman_numbers(self):
        roman_symbol_3 = "III"
        expected_roman_digit =3
        roman_solution_3 = Solution().romanToInt(roman_symbol_3)
        self.assertEqual(roman_solution_3, expected_roman_digit)

    def test_roman_numbers_58(self):
        roman_numbers_58 = "LVIII"
        expected_digit_58 = 58
        roman_solution_58 = Solution().romanToInt(roman_numbers_58)
        self.assertEqual(roman_solution_58, expected_digit_58)
if __name__ == "__main__":
    unittest.main()