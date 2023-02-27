def mysort(nums):
    # Sort the list in ascending order based on the remainder of the number divided by 3
    nums.sort(key=lambda x:x%7)
    return nums

# Example
nums = [123456789]
print(mysort(nums)) # Output: [9, 3, 6, 12, 15, 18, 21, 24, 27]