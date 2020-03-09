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

def double_char(str):
    final = ""
    for i in str:
        final += i + i
    return final

def count_hi(str):
    count = 0
    for i in range(0, len(str) - 1):
        if str[i:i+1] == "hi":
            count += 1
    return count

def cat_dog(str):
    catCount = 0
    dogCount = 0
    for i in range(0, len(str) - 2):
        if str[i:i+3] == "cat":
            catCount += 1
        if str[i:i+3] == "dog":
            dogCount += 1
    return catCount == dogCount

def count_code(str):
    count = 0
    for i in range(0, len(str) - 3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1
    return count

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) >= len(b):
        return a[len(a)-len(b):] == b
    else:
        return b[len(b)-len(a):] == a

def xyz_there(str):
    for i in range(len(str)-1, -1, -1):
        if str[i:i+3] == "xyz":
            if i == 0:
                return True
            else:
                return str[i - 1] != "."
    return False