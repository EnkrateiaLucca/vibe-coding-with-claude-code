#!/usr/bin/env python3
import os
import random
import time

class PythonQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the output of: print(type([]))?",
                "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
                "answer": 0
            },
            {
                "question": "Which method is used to add an element to the end of a list?",
                "options": ["add()", "append()", "insert()", "extend()"],
                "answer": 1
            },
            {
                "question": "What does the 'pass' statement do in Python?",
                "options": ["Exits the program", "Does nothing", "Skips the current iteration", "Raises an error"],
                "answer": 1
            },
            {
                "question": "What is the result of 3 * 'abc'?",
                "options": ["'3abc'", "'abcabcabc'", "SyntaxError", "TypeError"],
                "answer": 1
            },
            {
                "question": "Which of these is a mutable data type?",
                "options": ["tuple", "string", "list", "int"],
                "answer": 2
            },
            {
                "question": "What is the output of: bool('')?",
                "options": ["True", "False", "None", "Error"],
                "answer": 1
            },
            {
                "question": "Which keyword is used to create a generator function?",
                "options": ["return", "yield", "generate", "async"],
                "answer": 1
            },
            {
                "question": "What is list comprehension syntax for squares of numbers 0-4?",
                "options": ["[x**2 for x in range(5)]", "{x**2 for x in range(5)}", "(x**2 for x in range(5))", "[x**2 in range(5)]"],
                "answer": 0
            },
            {
                "question": "What does the @property decorator do?",
                "options": ["Makes a method static", "Creates a getter method", "Makes a method private", "Creates a class method"],
                "answer": 1
            },
            {
                "question": "What is the difference between '==' and 'is'?",
                "options": ["No difference", "'==' checks value, 'is' checks identity", "'is' checks value, '==' checks identity", "Both check type"],
                "answer": 1
            },
            {
                "question": "Which method removes and returns the last element from a list?",
                "options": ["remove()", "pop()", "delete()", "drop()"],
                "answer": 1
            },
            {
                "question": "What is the output of: len({'a': 1, 'b': 2, 'c': 3})?",
                "options": ["6", "3", "2", "Error"],
                "answer": 1
            },
            {
                "question": "How do you create an empty set in Python?",
                "options": ["{}", "set()", "[]", "()"],
                "answer": 1
            },
            {
                "question": "What is the purpose of __init__ method?",
                "options": ["Destroy object", "Initialize object", "Copy object", "Compare objects"],
                "answer": 1
            },
            {
                "question": "Which statement is used to handle exceptions?",
                "options": ["catch-throw", "try-except", "error-handle", "test-fail"],
                "answer": 1
            }
        ]
        self.score = 0
        self.current_question = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        print("\n" + "="*50)
        print("PYTHON PROGRAMMING QUIZ".center(50))
        print("="*50)
        print(f"\nQuestion {self.current_question + 1} of {len(self.questions)}")
        print(f"Score: {self.score}/{self.current_question}")
        print("-"*50 + "\n")
    
    def display_question(self, question_data):
        print(f"{question_data['question']}\n")
        for i, option in enumerate(question_data['options']):
            print(f"  {i+1}. {option}")
        print()
    
    def get_answer(self):
        while True:
            try:
                answer = input("Your answer (1-4): ").strip()
                if answer in ['1', '2', '3', '4']:
                    return int(answer) - 1
                print("Please enter a number between 1 and 4.")
            except KeyboardInterrupt:
                print("\n\nQuiz interrupted. Goodbye!")
                exit()
    
    def show_result(self, is_correct, correct_answer):
        print()
        if is_correct:
            print("✓ Correct!")
            self.score += 1
        else:
            print(f"✗ Wrong. The correct answer was: {correct_answer}")
        
        input("\nPress Enter to continue...")
    
    def show_final_score(self):
        self.clear_screen()
        percentage = (self.score / len(self.questions)) * 100
        
        print("\n" + "="*50)
        print("QUIZ COMPLETED!".center(50))
        print("="*50)
        print(f"\nFinal Score: {self.score}/{len(self.questions)} ({percentage:.1f}%)")
        
        if percentage >= 90:
            message = "Excellent! You're a Python master! 🐍"
        elif percentage >= 70:
            message = "Great job! Keep practicing!"
        elif percentage >= 50:
            message = "Good effort! Review the topics you missed."
        else:
            message = "Keep studying! Practice makes perfect."
        
        print(f"\n{message}")
        print("\n" + "="*50)
    
    def run(self):
        random.shuffle(self.questions)
        
        for i, question in enumerate(self.questions):
            self.current_question = i
            self.clear_screen()
            self.display_header()
            self.display_question(question)
            
            user_answer = self.get_answer()
            correct_answer = question['options'][question['answer']]
            is_correct = user_answer == question['answer']
            
            self.show_result(is_correct, correct_answer)
        
        self.show_final_score()

if __name__ == "__main__":
    quiz = PythonQuiz()
    
    print("\n" + "="*50)
    print("PYTHON PROGRAMMING QUIZ".center(50))
    print("="*50)
    print("\nTest your Python knowledge with 15 questions!")
    print("Each question has 4 options. Choose wisely!")
    print("\nPress Enter to start or Ctrl+C to exit...")
    
    try:
        input()
        quiz.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")