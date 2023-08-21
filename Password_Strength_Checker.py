import string

password = input("Please enter your password: ")

upper_case = any(1 if c in string.ascii_uppercase else 0 for c in password)
lower_case = any(1 if c in string.ascii_lowercase else 0 for c in password)
special = any(1 if c in string.punctuation else 0 for c in password)
digits = any(1 if c in string.digits else 0 for c in password)

characters = [upper_case, lower_case, special, digits]
length = len(password)
score = 0

with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print("Your password is too common. Please try again. Score: 0/7")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print(f"Password length is: {length}, adding {score} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password contains {sum(characters)} different character types, adding {sum(characters) - 1} points!")

if score < 4:
    print(f"Your password is weak! Score: {score} / 7")
elif score == 4:
    print(f"Your password is OK! Score: {score} / 7")
elif 4 < score < 6:
    print(f"Your password is pretty good! Score: {score} / 7")
elif score >= 6:
    print(f"Your password is strong! Score: {score} / 7")
