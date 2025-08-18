def binary_search_rotated(nums, target):
    #[4,5,6,7,8,0,1,2,3] start, end , mid =0, n-1 n= len(arr)
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1  

print(binary_search_rotated([4,5,6,7,0,1,2], 0))
