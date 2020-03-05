def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile

def monkey_trouble(a_smile, b_smile):
    return a_smile==b_smile

def sum_double(a, b):
    if a == b:
        return 4*a
    else:
        return a + b

def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10 (a, b):
    sum = a + b
    return sum == 10 or a == 10 or b == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return a < 0 and b > 0 or a > 0 and b < 0

def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str

def missing_char(str, n):
    return str[:n] + str[n+1:]

def front_back(str):
    length = len(str)
    if length > 1:
        return str[length-1] + str[1:length-1] + str[0]
    else:
        return str

def front3(str):
    if len(str) < 3:
        return str + str + str
    else:
        return str[:3] + str[:3] + str[:3]