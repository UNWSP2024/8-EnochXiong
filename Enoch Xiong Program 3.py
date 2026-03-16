import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Illinois": "Springfield",
    "New York": "Albany",
    "Texas": "Austin"
}

correct = 0
incorrect = 0

states = list(capitals.keys())

for i in range(5):
    state = random.choice(states)
    answer = input(f"What is the capital of {state}? ")

    if answer.lower() == capitals[state].lower():
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect. The correct answer is {capitals[state]}.")
        incorrect += 1

print("Quiz Finished!")
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)
