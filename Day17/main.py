from question_model import Question
from quiz_brain import QuizBrain


question_data = [
    {
        "text": "Python is a programming language.",
        "answer": "True"
    },
    {
        "text": "Python uses indentation to define blocks of code.",
        "answer": "True"
    },
    {
        "text": "The keyword used to create a function in Python is 'function'.",
        "answer": "False"
    },
    {
        "text": "A Python list can contain different data types.",
        "answer": "True"
    },
    {
        "text": "Python variable names can start with a number.",
        "answer": "False"
    },
    {
        "text": "The len() function is used to find the length of an object.",
        "answer": "True"
    },
    {
        "text": "A tuple in Python is mutable.",
        "answer": "False"
    },
    {
        "text": "The 'class' keyword is used to create a class in Python.",
        "answer": "True"
    },
    {
        "text": "The __init__() method is commonly used to initialize an object.",
        "answer": "True"
    },
    {
        "text": "A dictionary stores data using key-value pairs.",
        "answer": "True"
    },
    {
        "text": "A for loop can be used to iterate through a list.",
        "answer": "True"
    },
    {
        "text": "The input() function is used to get input from the user.",
        "answer": "True"
    },
    {
        "text": "Python is a case-sensitive programming language.",
        "answer": "True"
    },
    {
        "text": "The 'self' parameter is commonly used in Python class methods.",
        "answer": "True"
    },
    {
        "text": "A string in Python is written inside quotation marks.",
        "answer": "True"
    }
]


# Create Question objects
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

# Create QuizBrain object
quiz = QuizBrain(question_bank)


# Start the quiz
while quiz.still_has_questions():
    quiz.next_question()


# Final result
print("You've completed the quiz!")
print(f"Your final score was: "
      f"{quiz.score}/{quiz.question_number}.")
