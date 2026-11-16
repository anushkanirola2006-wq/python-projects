import time

print("Welcome to Anushka's Typing Challenge! ⌨️")
print("--------------------------------------")

sentence = "Python programming helps us develop logical thinking and creativity."

print("\nYou have 30 seconds!")
print("Type the following sentence as many times as possible:")
print(sentence)

input("\nPress Enter to start...")

start_time = time.time()
end_time = start_time + 30

typed_text = ""

while time.time() < end_time:
    remaining = end_time - time.time()
    print("\nTime left:", round(remaining), "seconds")

    text = input("Type here: ")
    typed_text += text + " "

    if time.time() >= end_time:
        break

total_time = time.time() - start_time

words = len(typed_text.split())

speed = (words / total_time) * 60

print("\n---------- YOUR RESULTS ----------")
print("Total words typed:", words)
print("Typing speed:", round(speed, 2), "WPM")
print("Time taken:", round(total_time, 2), "seconds")

print("\nWell done! ❤️")
with open("typing_results.txt", "a") as file:
    file.write(f"Words: {words}, Speed: {round(speed, 2)} WPM\n")

print("Your result has been saved! 💗")
with open("typing_results.txt", "r") as file:
    results = file.readlines()

speeds = []

for result in results:
    speed_value = result.split("Speed: ")[1]
    speed_value = speed_value.replace(" WPM", "")
    speeds.append(float(speed_value))

best_speed = max(speeds)

print("\n🏆 Your Personal Best:", best_speed, "WPM")