def make_bricks(small, big, goal):
    if big >= goal / 5:
        goal = goal % 5
    else:
        goal = goal - 5 * big
    if small >= goal:
        return True
    return False

def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c:
        sum += a
    if a != b and b != c:
        sum += b
    if a != c and b != c:
        sum += c
    return sum

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

def fix_teen(n):
    if n in range(13, 20) and n not in range(15, 17):
        return 0

def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c

def round10(num):
    if num % 10 >= 5:
        return num - num % 10 + 10
    else:
        return num - num % 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(a - c)
    diff3 = abs(b - c)
    return diff1 <= 1 and diff2 > 1 and diff3 > 1 or diff2 <= 1 and diff1 > 1 and diff3 > 1

def make_chocolate(small, big, goal):
    if big >= goal / 5:
        goal = goal % 5
    else:
        goal = goal - 5 * big
    if small >= goal:
        return goal
    return -1