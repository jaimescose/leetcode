"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def remove_duplicates(nums: list) -> int:
    """
    given a list of integers, it will remove de duplicates in-place without modifyin the original length.
    will return the final length of this list
    :param nums: list of integers
    :type nums: list
    :return: length result
    :rtype: int
    """

    i = 0
    for j in range(1, len(nums)):
        
        if nums[i] != nums[j]:
            # we assign the new number to i + 1 and move on
            nums[i + 1] = nums[j]
            i += 1

    return i + 1

# nums = [0,0,1,1,1,2,2,3,3,4]
# expected_nums = [0,1,2,3,4,'_','_','_','_','_']

nums = [1,1,2]
expected_nums = [1,2,'_']

k = remove_duplicates(nums)

print('the final length is:', k)
print('the final array is', nums)
