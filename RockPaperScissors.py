def rockPaperScissors():
    gameDict = {"rock" : 1, "paper" : 2,"scissors" : 3}
    play1 = input("Enter play 1: ").lower()
    play2 = input("Enter play 2: ").lower()
    a = gameDict.get(play1)
    b = gameDict.get(play2)

    if a - b in [-2, 1]:
        print("Player 1 wins! ")
    elif a - b in [-1, 2]:
        print("Player 2 wins! ")
    else:
        print("Tie! ")

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    rockPaperScissors()