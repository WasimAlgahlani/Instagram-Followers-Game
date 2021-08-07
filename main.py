"""Guess the number program"""
import random
from game_data import data


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
