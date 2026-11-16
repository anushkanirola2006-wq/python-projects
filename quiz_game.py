print("Welcome to Anushka's Quiz Game! ❤️")
print("-----------------------------")

score = 0

answer = input("1. Which language are we learning? ")

if answer.lower() == "python":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong answer!")

answer = input("2. What does HTML stand for? ")

if answer.lower() == "hypertext markup language":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong answer!")

answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong answer!")

print("-----------------------------")
print("Your final score is:", score, "/ 3")

if score == 3:
    print("Excellent! You are amazing! 🏆")
elif score == 2:
    print("Good job! ❤️")
else:
    print("Keep practising! 😊")