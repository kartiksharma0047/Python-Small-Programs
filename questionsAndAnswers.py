QueAndAns = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Pb", "Fe"],
        "answer": "Au"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    }
]
points = 0
print("Welcome to the Quiz!")
for index, i in enumerate(QueAndAns):
    print("Question", index + 1, ":", i["question"])
    print("Options:", end=" ")
    for j_index, j in enumerate(i["options"]):
        print("(" + str(j_index + 1) + ")", j, end=" ")
    userInput = int(input("\nEnter your answer: "))
    if i["options"][userInput - 1] == i["answer"]:
        points += 1
        print("Correct answer")
    else:
        print("Wrong answer")
print("Your total points are:", points)
