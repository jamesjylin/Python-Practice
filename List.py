def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    sum = 0
    for i in nums:
        sum += i
    return (sum - max(nums) - min(nums)) / (len(nums) - 2)

def sum13(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] != 13:
            sum += nums[i]
            i += 1
        else:
            i += 2
    return sum

def sum67(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            sum -= 7
            while nums[i] != 7:
                i += 1
        sum += nums[i]
        i += 1
    return sum

def has22(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False