def string_times(str, n):
    strFinal = ""
    for i in range(0,n):
        strFinal += str
    return strFinal

def front_times(str, n):
    final = ""
    if len(str) < 3:
        for i in range(0, n):
            final += str
    else:
        for i in range(0, n):
            final += str[:3]
    return final

def string_bits(str):
    final = ""
    for i in range (0, len(str), 2):
        final += str[i]
    return final

def string_splosion(str):
    final = ""
    for i in range (0, len(str) + 1):
        final += str[:i]
    return final

def last2(str):
    count = 0
    end = str[-2:]
    for i in range (0, len(str)-2):
        if str[i:i+2] == end:
            count += 1
    return count

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

def array_front9(nums):
    length = 4
    if len(nums) < 4:
        length = len(nums)
    for i in range (0, length):
        if nums[i] == 9:
            return True
    return False

def array123(nums):
    test = [1, 2, 3]
    for i in range (0, len(nums)):
        if test == nums[i:i+3]:
            return True
    return False

def string_match(a,b):
    length = len(a)
    if len(a) > len(b):
        length = len(b)
    count = 0
    for i in range (0, length-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count