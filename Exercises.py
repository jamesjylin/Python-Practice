import random

def charInput():
    age = int(input("How old are you? "))
    num = int(input("Give me another number: "))
    year = "" + str(2020 + age)
    print(num * ("You will be 100 by " + year + "\n"))

def evenOrOdd():
    num = int(input("Enter a number: "))
    if num % 4 == 0:
        print("Multiple of 4")
    elif num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    num2 = int(input("Enter another number: "))
    check = int (input("Enter a divisor: "))
    if num2 % check == 0:
        print("The divisor divides your number evenly.")

def listLessThan10():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(list(b for b in a if b < 5))
    num = int(input("Enter a number: "))
    print(list(b for b in a if b < num))

def divisors():
    num = int(input("Enter a number: "))
    print([divisor for divisor in range(1, num+1) if num % divisor == 0])

def listOverlap():
    a = sorted(random.choice(range(30)) for i in range(16))
    b = sorted(random.choice(range(30)) for i in range(12))
    print(a)
    print(b)
    print(list(c for c in set(a) if c in b))

def isPalindrome():
    string = input("Enter a string: ").lower().strip()
    flag = True
    for i in range(0, len(string)):
        if string[i] != string[len(string)-i-1]:
            print("Not a palindrome.")
            flag = False
            break
    if flag:
        print("A palindrome!")

def listEven():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([b for b in a if b % 2 == 0])

def guessingGame():
    randomNum = int(random.randint(1, 10))
    guess = 0
    guessCount = 0
    while guess != randomNum:
        guess = input("Guess a number from 1 to 9 or type exit: ")
        if guess == "exit":
            break
        guessCount += 1
        if int(guess) < randomNum:
            print("Too low. ")
        elif int(guess) > randomNum:
            print("Too high. ")
        else:
            print("You got it! ")
            break
    print("Number of guesses: " + str(guessCount))

def isPrime():
    num = int(input("Enter a number: "))
    prime = True
    for a in range(2, num):
        if num % a == 0:
            prime = False
            break
    if not prime or num == 1:
        print("Not a prime! ")
    else:
        print("Prime! ")

def listEnds():
    a = sorted(random.choice(range(30)) for i in range(10))
    print(a)
    print([a[0], a[len(a) - 1]])

def fibonacci1(n):
    if n <= 1:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci():
    num = int(input("Enter a number: "))
    for i in range(num):
        print(fibonacci1(i), end = ", ")


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    fibonacci()