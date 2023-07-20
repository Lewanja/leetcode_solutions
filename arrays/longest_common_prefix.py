from typing import List

#list of strings
# get the first item in the list
# get first letter of first string gotten from initial list
# if letter is present in first word
# then check the next letter
# repeat the step above with second letter of word in list

# strs = ["flower","flow","flight"]
# first_word = strs.pop(0)
# letter_index = 0
# common_prefix = ""
#
# for word in strs:
#
#     first_letter_first_word = first_word[letter_index]
#
#     if first_letter_first_word != word[letter_index]:
#         print("")
#     else:
#         common_prefix += first_letter_first_word
#     letter_index += 1
# print(common_prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:

            first_word = strs.pop(0)
            letter_index = 0
            common_prefix = ""

            for word in strs:
                first_letter_first_word = first_word[letter_index]

                if first_letter_first_word != word[letter_index]:
                    return ("")
                else:
                    common_prefix += first_letter_first_word

                letter_index += 1
            return (common_prefix)

ans = Solution().longestCommonPrefix(["", ""])
print(ans)