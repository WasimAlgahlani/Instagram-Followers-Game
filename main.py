"""Guess the number program"""
import random
from game_data import data

# def check(num, attempts):
#     """Code"""
#     while attempts > 0:
#         print(f"You have {attempts} remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         if guess > num:
#             print("Too high.")
#         elif guess < num:
#             print("Too low.")
#         else:
#             print(f"You got it! The answer was {num}.")
#             break
#         if guess > num or guess < num and attempts > 1:
#             print("Guess again.")
#         attempts -= 1
#     if attempts == 0:
#         print(f"You've run out of guesses, you lose, the number was {num}.")
#
#
# def game():
#     """main"""
#     print("Welcome to the guessing number game.\nI'm thinking of a number between 1 and 100.")
#     number = random.randint(1, 100)
#     dif = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if dif == "hard":
#         check(number, 5)
#     elif dif == "easy":
#         check(number, 10)
#     else:
#         print("Wrong choice")
#
#
# game()


def check(guess_f, account_a_f, account_b_f):
    if account_a_f['follower_count'] > account_b_f['follower_count']:
        return "a"
    else:
        return "b"


con = True
score = 0
account_a = random.choice(data)
while con:
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.\n")
    print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.\n")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print()
    if check(guess, account_a, account_b) == guess:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        con = False
        print(f"You're Wrong! Current score: {score}.\n")
    account_a = account_b
    print("\n\n")
