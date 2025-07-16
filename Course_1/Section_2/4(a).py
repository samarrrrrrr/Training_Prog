"""
1. Create a guessing game:
    Pick any integer from the range 1 - 100
    Ask the user for input to guess an integer in the range from 1 - 100
    Give them 5 guesses
    Provide the user feedback on whether the guess is too high or too low, per guess
    If they get the correct answer, display a message telling them the number of guesses it took.
    If they do not get the answer within 5 guesses, display the answer.
    End the program
"""
ans = 50
for i in range(0,5) :
    user_input = int(input("Enter a number: "))
    if user_input == ans :
        print("It took you", i+1, "number of guesses")
    else :
        if abs(user_input-ans) > 10 :
            print("too high")
        elif abs(user_input-ans) <= 10 :
            print("close")
print("The answer was", ans)