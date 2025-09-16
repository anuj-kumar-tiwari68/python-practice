nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# left = 0
# right = len(nums) - 1

def rev(nums,left,right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    rev(nums,left+1,right-1)

arr1 = nums[:]
rev(arr1,2,5)
print(arr1)

